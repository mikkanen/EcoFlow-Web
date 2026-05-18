from flask import Flask, render_template, jsonify
from teamlead.pw.ecoflow.api import EcoflowApi
import os

# --- ASETUKSET ---
# Haetaan tiedot ympäristömuuttujista, jotta ne ovat turvassa.
# Voit myös kovakoodata ne tähän testauksen ajaksi.
ECOFLOW_ACCESS_KEY = os.environ.get("ECOFLOW_ACCESS_KEY", "OMA_ACCESS_KEY")
ECOFLOW_SECRET_KEY = os.environ.get("ECOFLOW_SECRET_KEY", "OMA_SECRET_KEY")
DELTA_PRO_SERIAL_NUMBER = os.environ.get("ECOFLOW_SN", "OMA_DELTA_PRO_SN")

app = Flask(__name__)

# --- DATAN HAKUFUNKTIO ---
def fetch_ecoflow_data():
    """Hakee ja palauttaa EcoFlow-datan sanakirjana."""
    try:
        api = EcoflowApi(access_key=ECOFLOW_ACCESS_KEY, secret_key=ECOFLOW_SECRET_KEY)
        quota_response = api.get_device_quota_all(DELTA_PRO_SERIAL_NUMBER)
        params = quota_response.json().get('data', {})
        
        data = {
            "voltage": params.get('mppt.inVol', 0) / 10,
            "current": params.get('mppt.inAmp', 0) / 100,
            "power": params.get('mppt.inWatts', 0) / 10,
            "soc": params.get('pd.soc', 0), # LISÄTTY TÄMÄ RIVI
            "input_total": params.get('pd.wattsInSum', 0),
            "output_total": params.get('pd.wattsOutSum', 0)
        }
        return data
    except Exception as e:
        print(f"Virhe datan haussa: {e}")
        return None

# --- WEB-SIVUN REITIT ---

@app.route('/')
def index():
    """Näyttää pääsivun (index.html)."""
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    """Tarjoaa datan JSON-muodossa, jota web-sivu voi kutsua."""
    data = fetch_ecoflow_data()
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Datan haku epäonnistui"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)