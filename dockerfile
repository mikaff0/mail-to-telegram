# Verwende ein Python-Image als Basis
FROM python:3.9-slim

# Arbeitsverzeichnis im Container setzen
WORKDIR /app

# Abhängigkeiten installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Skript kopieren
COPY script.py .

# Container starten
CMD ["python", "script.py"]
