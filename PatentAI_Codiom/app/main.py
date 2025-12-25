# app/main.py

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware  # CORS için
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session

from app.core.config import settings
from . import models
from .database import engine, SessionLocal
from .ai_models import llm_service

# database tablolarını oluşturuyor
models.Base.metadata.create_all(bind=engine)

# --- Pydantic Modelleri (API Kontratı) ---
class AnalysisRequest(BaseModel):
    text_to_analyze: str
    analysis_level: str = "deep"

class SimilarPatent(BaseModel):
    patent_id: str
    title: str
    similarity_score: float

class AnalysisResponse(BaseModel):
    analysis_id: str
    status: str
    novelty_score: float
    similar_patents: List[SimilarPatent]
    summary: str

# --- Veritabanı Bağımlılığı ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- FastAPI Uygulaması ---
app = FastAPI(title=settings.PROJECT_NAME)

# --- bunlar CORS ayarları ---
# Bu blok, frontend'den (tarayıcıdan) gelen isteklere
# API'mizin cevap vermesine izin verir.
origins = [
    "*",  # şimdilik tüm adreslere izin veriyor geliştirme için
    "null" # file:// yani dosyadan açılan html için bu gerekli
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- CORS AYARLARI bitti ---


# --- API UÇ NOKTALARI ---
@app.get("/")
def read_root():
    return {"message": f"{settings.PROJECT_NAME} API'sine hoş geldiniz!"}


@app.post("/api/analyze", response_model=AnalysisResponse)
async def analyze_patent_idea(request: AnalysisRequest, db: Session = Depends(get_db)):
    """
    Patent fikrini alır, YENİ LLM SERVİSİMİZ ile analiz eder,
    sonucu veritabanına kaydeder ve kullanıcıya döndürür.
    """
    print(f"Analiz için gelen metin: '{request.text_to_analyze}'")

    # 1. YENİ YAPAY ZEKA SERVİSİNİ ÇAĞIR
    #    Artık mock_response yok!
    analysis_result = llm_service.get_analysis(request.text_to_analyze)

    # 2. VERİTABANINA KAYDET
    #    Yapay zekadan gelen gerçek sonuçları kaydet
    db_report = models.AnalysisReport(
        text_to_analyze=request.text_to_analyze,
        novelty_score=analysis_result["novelty_score"],
        summary=analysis_result["summary"]
    )

    db.add(db_report)
    db.commit()
    db.refresh(db_report)

    print(f"Rapor başarıyla veritabanına kaydedildi, ID: {db_report.id}")

    # 3. KULLANICIYA CEVABI DÖNDÜR
    #    Cevabı, veritabanından ve AI servisinden gelen
    #    gerçek verilerle oluştur.
    return AnalysisResponse(
        analysis_id=str(db_report.id),  # DB'den gelen gerçek ID
        status="completed",
        novelty_score=analysis_result["novelty_score"],
        summary=analysis_result["summary"],
        similar_patents=[]  # Benzer patent işini daha yapmadık
    )