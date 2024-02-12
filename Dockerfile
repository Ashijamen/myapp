# Wersja obrazu Python
FROM python:3.8

# Katalog roboczy
WORKDIR /app

# Kopiowanie plików do kontynera
COPY . /app

# Instaluj zależności
RUN apt-get update \
    && apt-get install -y build-essential \
    && pip install --upgrade pip \
    && pip install Flask SQLAlchemy python-dotenv \
    && apt-get remove -y build-essential \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Uruchom aplikację
CMD ["python", "app.py"]
