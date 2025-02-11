FROM python:3.13

RUN apt-get update && apt-get install -y \
    libnss3 \
    libgtk-3-0 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando padrão para iniciar a aplicação
CMD ["python", "app/main.py"]
