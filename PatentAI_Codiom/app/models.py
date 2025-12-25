# app/models.py

from sqlalchemy import Column, Integer, String, Float
from .database import Base

# database.py'da oluşturduğumuz Base sınıfını miras alıyoz
# SQLAlchemy bu sayede bu sınıfın bir veritabanı tablosuna karşılık geldiğini anlar.
class AnalysisReport(Base):
    # bu modelin veritabanındaki tablo ismini yazıyoruz
    __tablename__ = "analysis_reports"

    # tablo sütunlarını tanımlıyoruz
    
    # id: her rapor için kimlik gibi bi sayı, kendi kendine artıyo
    # primary_key=True, bu sütunun primary key olduğunu belirtiyo (her satır için eşsiz)
    # index=True, bu sütuna göre arama yapmayı hızlandırır.
    id = Column(Integer, primary_key=True, index=True)

    # text_to_analyze: bunu kullanıcı giriyor ve bu metin ve analiz edilen metin oluyo
    text_to_analyze = Column(String)

    # novelty_score: Analiz sonucu üretilen yenilik skoru (ondalıklı sayı).
    novelty_score = Column(Float)

    # summary: Analiz sonucu üretilen özet metin.
    summary = Column(String)