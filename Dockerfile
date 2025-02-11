FROM python:3.13

RUN apt-get update && apt-get install -y \
    libnss3 \
    libgtk-3-0 \
    libasound2 \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    && rm -rf /var/lib/apt/lists/*


RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/microsoft.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/edge stable main" \
    > /etc/apt/sources.list.d/microsoft-edge.list

RUN apt-get update && apt-get install -y microsoft-edge-stable

WORKDIR /rpa

ENV PYTHONPATH=/rpa

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "rpa.app/main.py"]
