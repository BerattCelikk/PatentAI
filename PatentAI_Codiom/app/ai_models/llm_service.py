# app/ai_models/llm_service.py

import faiss
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import os

# --- 1. DOSYA YOLLARINI VE PARAMETRELERİ TANIMLA ---
INDEX_PATH = 'data/vectors/patent_embeddings.faiss'
CSV_PATH = 'data/processed/patentAI.csv'
MODEL_NAME = 'all-MiniLM-L6-v2'
TOP_K = 3  # Kullanıcının metnine en çok benzeyen kaç patent bulmak istiyoruz?

# --- 2. MODELLERİ VE VERİYİ GLOBAL KAPSAMDA YÜKLE ---
# Bu, API her çağrıldığında değil, SADECE BİR KEZ (uygulama başlarken)
# yüklenmelerini sağlar. Bu çok önemlidir.

def load_data():
    """Veriyi ve modelleri hafızaya yükler."""
    
    print(f"FAISS indeksi yükleniyor: {INDEX_PATH}...")
    if not os.path.exists(INDEX_PATH):
        print(f"HATA: FAISS indeksi bulunamadı: {INDEX_PATH}")
        print("Lütfen önce 'data/vectors/vectors.py' script'ini çalıştırdığınızdan emin olun.")
        return None, None, None
    
    index = faiss.read_index(INDEX_PATH)
    
    print(f"CSV verisi yükleniyor: {CSV_PATH}...")
    if not os.path.exists(CSV_PATH):
        print(f"HATA: CSV dosyası bulunamadı: {CSV_PATH}")
        return None, None, None
            
    # FAISS bize sadece '5' gibi bir ID verecek.
    # O ID'nin hangi patent olduğunu bilmek için 'title' sütununu hafızaya alıyoruz.
    try:
        df = pd.read_csv(CSV_PATH)
        if 'title' not in df.columns:
            print("HATA: CSV dosyasında 'title' sütunu bulunamadı.")
            return None, None, None
            
        df['title'] = df['title'].fillna('')  # Boş değerleri temizle
        patent_titles = df['title'].tolist()
    except Exception as e:
        print(f"CSV okuma hatası: {e}")
        return None, None, None

    print(f"Dil modeli yükleniyor: {MODEL_NAME}...")
    model = SentenceTransformer(MODEL_NAME)
    
    print("Tüm modeller ve veriler başarıyla yüklendi.")
    return index, model, patent_titles

# Uygulama başlarken her şeyi yükle
faiss_index, sentence_model, patent_titles = load_data()

# --- 3. GÜNCELLENMİŞ ANALİZ FONKSİYONU ---

def get_analysis(text: str) -> dict:
    """
    Artık sahte bekleme yok. Gerçek FAISS araması yapar.
    (Not: 'async def' değil, 'def' yaptık çünkü arama işlemi CPU-yoğun)
    """
    
    if faiss_index is None:
        # Modeller yüklenememişse hata döndür
        return {
            "novelty_score": 0.0,
            "summary": "HATA: Sunucu taraflı model veya veri yüklenemedi. Lütfen yöneticiye başvurun."
        }

    print(f"Gerçek Benzerlik Araması Başlatıldı... (Metin: {text[:20]}...)")

    # 1. Gelen metni vektöre dönüştür
    query_vector = sentence_model.encode([text])
    query_vector = np.array(query_vector).astype('float32')

    # 2. FAISS içinde en benzer K adet vektörü ara
    # D = mesafeler, I = indeksler (bizim aradığımız bu)
    distances, indices = faiss_index.search(query_vector, TOP_K)
    
    # 3. Bulunan indekslere (ID'lere) karşılık gelen patent başlıklarını al
    found_patents = []
    for i in indices[0]:
        if i != -1:  # -1, geçerli bir sonuç bulunamadı demektir
            found_patents.append(patent_titles[i])
    
    print(f"Benzer {len(found_patents)} patent bulundu.")

    # 4. Sonucu formatla (LLM arkadaşının görevi için hazırla)
    if not found_patents:
        summary = "Analiziniz tamamlandı. Veritabanımızda metninize benzer bir patente rastlanmadı. Bu yüksek bir yenilik potansiyeline işaret edebilir!"
    else:
        # LLM arkadaşın ileride bu 'found_patents' listesini alıp
        # 'text' ile karşılaştırıp özet çıkaracak.
        # ŞİMDİLİK, sadece bulduklarımızı listeleyelim.
        summary = "Analiziniz tamamlandı. Fikrinize benzer patentler bulundu:\n\n* " + "\n* ".join(found_patents)

    # Sahte bir skor üretelim (1.0 - en yakın mesafe = benzerlik skoru)
    novelty_score = (1.0 - distances[0][0]) * 100 

    return {
        "novelty_score": novelty_score,
        "summary": summary
    }