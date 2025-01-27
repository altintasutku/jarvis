FROM python:3.9-slim

# Sistem bağımlılıklarını kur
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    python3-pyaudio \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Çalışma dizinini oluştur
WORKDIR /app

# Python bağımlılıklarını kopyala ve kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ollama'yı kur
RUN curl -L https://ollama.ai/download/ollama-linux-amd64 -o /usr/local/bin/ollama \
    && chmod +x /usr/local/bin/ollama

# Uygulama kodunu kopyala
COPY main.py .

# Ollama'yı başlat ve modelleri indir
RUN ollama serve & \
    sleep 5 && \
    ollama pull llama3.2:1b && \
    ollama pull deepseek-r1:8b

# Uygulamayı çalıştır
CMD ["python", "main.py"] 