// === TEMA GEÇİŞİ ===
const themeBtn = document.getElementById('themeToggle');
const body = document.body;

if (localStorage.getItem('theme') === 'dark') {
  body.classList.add('dark');
  themeBtn.textContent = '☀️';
}

themeBtn.addEventListener('click', () => {
  body.classList.toggle('dark');
  if (body.classList.contains('dark')) {
    themeBtn.textContent = '☀️';
    localStorage.setItem('theme', 'dark');
  } else {
    themeBtn.textContent = '🌙';
    localStorage.setItem('theme', 'light');
  }
});

// === CHAT (Gerçek API Bağlantısı) ===
const sendBtn = document.getElementById('sendBtn');
const userInput = document.getElementById('userInput');
const chatBox = document.getElementById('chatBox');

// Gönder tuşu tıklandığında
sendBtn.addEventListener('click', () => {
  sendMessage();
});

// Enter tuşu basıldığında
userInput.addEventListener('keypress', (event) => {
  if (event.key === 'Enter') {
    sendMessage();
  }
});

async function sendMessage() {
  const message = userInput.value.trim();
  if (message === '') return;

  // 1. Kullanıcının mesajını ekrana bas
  addMessage('user', message);
  userInput.value = '';

  try {
    // 2. Bizim FastAPI Back-end'imize isteği gönder
    const response = await fetch('http://127.0.0.1:8000/api/analyze', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      // API'mizin beklediği formata (AnalysisRequest modeli) uygun JSON gönder
      body: JSON.stringify({
        text_to_analyze: message,
        analysis_level: 'deep' // Bunu şimdilik sabit yollayabiliriz
      }),
    });

    if (!response.ok) {
      // Sunucudan 404, 500 gibi bir hata dönerse
      throw new Error(`HTTP hatası! Durum: ${response.status}`);
    }

    // 3. Back-end'den gelen cevabı JSON olarak al
    const data = await response.json();

    // 4. Gelen cevaptaki 'summary' (özet) kısmını bota yazdır
    //    (data.summary bizim AnalysisResponse modelimizdeki 'summary' alanı)
    addMessage('bot', data.summary);

  } catch (error) {
    // 5. Bir hata olursa (sunucu çalışmıyorsa veya CORS hatası varsa)
    console.error('API isteği başarısız:', error);
    addMessage('bot', 'Üzgünüm, sunucuya bağlanırken bir hata oluştu. 😥');
  }
}

function addMessage(sender, text) {
  const msgDiv = document.createElement('div');
  msgDiv.classList.add('message', sender);
  msgDiv.innerHTML = `<div class="bubble">${text}</div>`;
  chatBox.appendChild(msgDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}