import requests

url = "http://127.0.0.1:8000/predict"
payload = {
    "features": [6, 148, 72, 35, 0, 33.6, 0.627, 50]
}

# comments
response = requests.post(url, json=payload)
print(f"status_code:{response.status_code}, la valeur de la prediction: {response.json()["prediction"]} ET le résultat de l'API: {response.json()}")  # Résultat attendu : {"prediction": 1}

# curl -X POST http://127.0.0.1:5000/predict \
#   -H "Content-Type: application/json" \
#   -d '{"features": [6, 148, 72, 35, 0, 33.6, 0.627, 50]}'