# Käytetään kevyttä Python 3.11 -pohjaa
FROM python:3.11-slim

# Asetetaan työkansio kontin sisällä
WORKDIR /app

# Kopioidaan riippuvuudet ja asennetaan ne
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopioidaan sovelluksen koodi ja templatet
COPY app.py .
COPY templates templates

# Asetetaan ympäristömuuttujat (Nämä annetaan myöhemmin Docker-komennossa)
ENV ECOFLOW_ACCESS_KEY=""
ENV ECOFLOW_SECRET_KEY=""
ENV ECOFLOW_SN=""

# Kerrotaan Dockerille, että kontti kuuntelee porttia 5000
EXPOSE 5000

# Komento, joka suoritetaan, kun kontti käynnistyy
CMD ["flask", "run", "--host=0.0.0.0"]