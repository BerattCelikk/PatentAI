<div id="top">

<div align="center">

<div align="center">
  <img src="https://github.com/user-attachments/assets/51fd7451-e708-4fd2-a70e-caac8746781a" width="300" height="300" alt="WaterTwin AI Dashboard">
</div>

# <code>Patent AI</code>

**CODIOM**

<em>Technologies to be Used:</em>

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=Flask&logoColor=white" alt="Flask">
<img src="https://img.shields.io/badge/SentenceTransformers-FF6F00.svg?style=for-the-badge&logo=HuggingFace&logoColor=white" alt="SentenceTransformers">
<img src="https://img.shields.io/badge/FAISS-00B0FF.svg?style=for-the-badge&logo=Facebook&logoColor=white" alt="FAISS">
<img src="https://img.shields.io/badge/scikit--learn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
<img src="https://img.shields.io/badge/Llama-3B82F6.svg?style=for-the-badge&logo=Meta&logoColor=white" alt="Llama">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5">
<img src="https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white" alt="CSS3">


</div>
<br>

---

##  Table of Contents
- [ Overview](#️-overview)
- [ Team](#-team)
- [ Problem](#-problem)
- [ Solution](#-solution)
- [ Key Features](#-key-features)
- [ Tech Stack](#-tech-stack)
- [ System Architecture](#️-system-architecture)
- [ Data Sources](#-data-sources)
- [ Roadmap](#️-roadmap)
---

## Overview

**Patent AI** is an intelligent, AI-driven platform designed to act as a **"Patent Difference Analysis and Innovation Consultant."**

The traditional patent research process is often long, complex, and prohibitively expensive. Entrepreneurs, researchers, and R&D teams struggle to determine if their ideas are truly novel, frequently relying on systems that only support English or offer basic keyword-based search results without intelligent context.

**Patent AI transforms this process by:**
* **Semantic Analysis:** Utilizing Deep Learning and Vector Search (FAISS, SentenceTransformers) to understand the *meaning* of an invention, not just the keywords.
* **Difference Detection:** Automatically comparing user ideas against existing patent databases to highlight specific similarities and unique differentiators.
* **Bilingual Support:** bridging a critical gap by providing native support for **Turkish** patent data alongside global English databases.
* **Smart Consultation:** Leveraging LLMs (Llama 3/GPT-4) to evaluate innovation potential and provide strategic, actionable recommendations.

## 👥 Ekip


| Rol | Üye | LinkedIn |
|------|--------|-----------|
| **Deep Learning & Team Lead** | Berat Erol Çelik | [![LinkedIn](https://img.shields.io/badge/-Berat_Erol_Çelik-0077B5?style=flat-square&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/berat-erol-%C3%A7elik-513915258/) |
| **Backend & API** | Emre Aldemir | [![LinkedIn](https://img.shields.io/badge/-Emre_Aldemir-0077B5?style=flat-square&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/emre-aldemir-1b2301293/) |
| **Frontend & UI/UX** | Umut Odabaş | [![LinkedIn](https://img.shields.io/badge/-Umut_Odabaş-0077B5?style=flat-square&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/umut-odaba%C5%9F-8a26142a2/) |
| **Machine Learning** | Ömer Altıntaş | [![LinkedIn](https://img.shields.io/badge/-Ömer_Altıntaş-0077B5?style=flat-square&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/%C3%B6mer-alt%C4%B1nta%C5%9F-44773730b/) |
| **LLM Specialist** | Efkan Çıtak | [![LinkedIn](https://img.shields.io/badge/-Efkan_Çıtak-0077B5?style=flat-square&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/efkan-%C3%A7%C4%B1tak-b848a32a0/) |

---

## 🎯 Problem
Patent süreçleri uzun, karmaşık ve maliyetlidir. Girişimciler, araştırmacılar veya Ar-Ge ekipleri, fikirlerinin daha önce patentlenip patentlenmediğini, hangi alanlarda yoğun başvuru olduğunu veya hangi kısmının gerçekten yenilik taşıdığını anlamakta zorlanıyor.  
Mevcut sistemler:  
- Yalnızca İngilizce çalışıyor, Türkçe patent verilerini kapsamaz.  
- Sadece arama yapan araçlar seviyesinde kalıyor, kullanıcıya akıllı öneriler sunmuyor.  
- Patent sonrası benzer başvuruları takip etmiyor.  

---

## 💡 Çözüm

PatentAI
- Fikri veya patent dokümanını analiz eder
- Benzer patentleri bulur ve farklarını özetler
- Yenilik potansiyelini değerlendirir
- Girişimciler, Ar-Ge Ekipleri ve araştırmacıları için akıllı öneriler sunar

---

## 🚀 Temel Özellikler

| Özellik | Açıklama | Durum |
|---------|-------------|---------|
| 🔍 **Patent Fark Analizi** | Fikirleri mevcut patentlerle karşılaştırır | ❌ Planlama |
| 🧠 **LLM Tabanlı Anlamsal Analiz** | Llama 3/GPT-4 ile akıllı yorumlama | ❌ Planlama |
| 💡 **Patentlenebilirlik Değerlendirmesi** | Yenilik potansiyelini değerlendirir | ❌ Planlama |
| 🌐 **Türkçe Patent Desteği** | Türkçe patent analizi yapan ilk sistem | ❌ Planlama |
| 📊 **Yoğunluk & Boşluk Analizi** | Kalabalık ve boş teknoloji alanlarını belirler | ❌ Planlama |
| 🔔 **Patent İzleme** | Patent sonrası benzer başvuruları takip eder | ❌ Planlama |
| 🎯 **Stratejik Öneriler** | Teknik ve pazar odaklı tavsiyeler | ❌ Planlama |
| 👥 **Çok Kullanıcılı Raporlar** | Farklı kullanıcı tipleri için özel raporlar | ❌ Planlama |


    
---

## 🔧 Teknoloji Yığını

### Backend & API
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=Flask&logoColor=white" alt="Flask">

### Yapay Zeka & Makine Öğrenmesi
<img src="https://img.shields.io/badge/SentenceTransformers-FF6F00.svg?style=for-the-badge&logo=HuggingFace&logoColor=white" alt="SentenceTransformers">
<img src="https://img.shields.io/badge/FAISS-00B0FF.svg?style=for-the-badge&logo=Facebook&logoColor=white" alt="FAISS">
<img src="https://img.shields.io/badge/scikit--learn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
<img src="https://img.shields.io/badge/Llama-3B82F6.svg?style=for-the-badge&logo=Meta&logoColor=white" alt="Llama">

### Önyüz & Kullanıcı Arayüzü
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5">
<img src="https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white" alt="CSS3">

### Veritabanı & Dağıtım
<img src="https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=for-the-badge&logo=PostgreSQL&logoColor=white" alt="PostgreSQL">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Render-46E3B7.svg?style=for-the-badge&logo=Render&logoColor=white" alt="Render">

---

## 🏗️ Sistem Mimarisi


Patent AI, yapay zekâ destekli bir “patent fark analizi ve yenilik danışmanı”dır. Sistem, girilen fikri veya patent dokümanını analiz eder, mevcut patentlerle kıyaslar, farklarını bulur ve yenilik potansiyelini değerlendirir.

```sh
└── /
    ├── ai_models
    │   ├── embeddings
    │   ├── evaluation
    │   ├── llm_analysis
    │   └── similarity
    ├── backend
    │   └── app
    ├── data
    │   ├── processed
    │   ├── raw
    │   └── vectors
    ├── deployment
    │   └── deployment.py
    ├── docs
    │   ├── api
    │   ├── technical
    │   └── user_guide
    └── frontend
        ├── assets
        └── components
```

### API Uç Noktaları
| Uç Nokta | Metot | Açıklama |
|----------|--------|-------------|
| `/api/analyze` | POST | Patent fikrini analiz eder ve benzerlikleri bulur |
| `/api/similar` | GET | Benzer patentleri bulur |
| `/api/report` | POST | Analiz raporu oluşturur |
| `/api/health` | GET | Sistem sağlık kontrolü |

### Veri Akışı
1. **Girdi**: Kullanıcı fikir/patent metni gönderir
2. **İşleme**: Metin SentenceTransformers ile vektörlere dönüştürülür
3. **Arama**: FAISS benzerlik araması ile patent veritabanında tarama
4. **Analiz**: LLM farkları ve yenilik potansiyelini işler
5. **Çıktı**: Öneriler içeren yapılandırılmış rapor

---

## 📊 Veri Kaynakları

PatentAI, hem Türkçe hem İngilizce patent verileriyle çalışır.  
İlk MVP sürümünde kullanılacak kaynaklar:

- **Google Patent İngilizce ve Türkçe Patentler** - Ana veri kaynağı
- **EPO (European Patent Office)** - Ana veri kaynağı

## 🗓️ Yol Haritası
-  **`Task 1`**: Analiz & Planlama
-  **`Task 2`**: Veri Toplama & Modelleme Başlangıcı
-  **`Task 3`**: Flask API & Backend Geliştirme
-  **`Task 4`**: Arayüz + Raporlama ( Python tabanlı)
-  **`Task 5`**: Test,Demo & Sunum


**Teknolojiler:**  
- Python 3.x  
- Flask / FastAPI  
- SentenceTransformers (`all-MiniLM-L6-v2`)  
- FAISS veya cosine similarity  
- PostgreSQL (veri kayıtları)  
- Opsiyonel: Elasticsearch (hızlı metin araması için)

---

### Example Data Flow

1. Kullanıcı fikir veya patent özetini girer.  
2. Backend, metni embedding’e çevirir (`SentenceTransformers`).  
3. Benzer patentleri veritabanında arar (`cosine similarity` / `faiss`).  
4. LLM (ör. Llama 3 veya GPT-4) farkları ve yenilik yönlerini yorumlar.  
5. Sonuçlar JSON veya HTML raporu olarak frontend’e döner.

---


[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
















