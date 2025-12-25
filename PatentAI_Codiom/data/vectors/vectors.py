# VEKTÖR VERİLERİ - AI için optimize edilmiş veriler
# patent_embeddings.faiss - FAISS vektör veritabanı
# embedding_cache.pkl - Önceden hesaplanmış embedding'ler
# vector_index/ - Hızlı arama için indekslenmiş vektörler
# similarity_matrix/ - Benzerlik matrisleri

import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

# --- 1. Dosya Yollarını Tanımla ---
# Projenin ana klasörüne göre yolları belirle
# (Bu script'i ana klasörden (patent-ai-backend) çalıştırmalıyız)
CSV_PATH = 'data/processed/patentAI.csv'
INDEX_PATH = 'data/vectors/patent_embeddings.faiss'

def create_vector_database():
    """
    patentAI.csv dosyasını okur, 'title' sütununu vektöre dönüştürür
    ve bir FAISS indeksi olarak kaydeder.
    """
    
    # --- 2. Veriyi Oku ---
    print(f"Veri okunuyor: {CSV_PATH}")
    if not os.path.exists(CSV_PATH):
        print(f"HATA: CSV dosyası bulunamadı: {CSV_PATH}")
        print("Lütfen script'i projenin ana klasöründen (patent-ai-backend) çalıştırdığınızdan emin olun.")
        return

    try:
        df = pd.read_csv(CSV_PATH)
    except Exception as e:
        print(f"CSV okuma hatası: {e}")
        return
        
    # 'title' sütununun var olduğundan emin ol
    if 'title' not in df.columns:
        print("HATA: CSV dosyasında 'title' sütunu bulunamadı.")
        return
        
    # 'title' sütunundaki boş (NaN) değerleri temizle
    df['title'] = df['title'].fillna('')
    texts = df['title'].tolist()
    
    print(f"Toplam {len(texts)} adet patent metni okundu.")

    # --- 3. Modeli Yükle ve Vektörleri Oluştur ---
    # Readme'de belirtilen modeli kullanalım
    print("Dil modeli yükleniyor (all-MiniLM-L6-v2)... Bu işlem biraz sürebilir.")
    model = SentenceTransformer('all-MiniLM-L6-v2') 
    
    print("Metinler vektörlere dönüştürülüyor (Embedding)...")
    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings).astype('float32') # FAISS float32 ister

    print(f"Vektörler oluşturuldu. Boyut: {embeddings.shape}")

    # --- 4. FAISS İndeksi Oluştur ve Kaydet ---
    d = embeddings.shape[1]  # Vektör boyutu
    index = faiss.IndexFlatL2(d) # L2 (Euclidean) mesafesi kullanan basit bir indeks
    
    print("Vektörler FAISS indeksine ekleniyor...")
    index.add(embeddings)
    
    print(f"İndeks FAISS dosyasına kaydediliyor: {INDEX_PATH}")
    faiss.write_index(index, INDEX_PATH)
    
    print("\nİşlem Tamamlandı!")
    print(f"'{INDEX_PATH}' başarıyla oluşturuldu.")

# Bu script doğrudan çalıştırılırsa, create_vector_database fonksiyonunu çağır
if __name__ == "__main__":
    create_vector_database()