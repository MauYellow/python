from flask import Flask, jsonify
import requests

app = Flask(__name__)

AirtableAPIKey = "patmwWf2nhxbqK0l4.ff8ce9c4a82d639ceda9bb3f690f1b8d8663a339dd25f0626b9011c02b7016e7"

@app.route("/")
def home():
    return "L'applicazione è in esecuzione!"

@app.route("/send_message/<message>")
def send_message(message):
    url = "https://api.telegram.org/bot8152616899:AAFdwcDFkiDoxzWz22ziGqhI70mR1EieHzo/sendMessage"
    data = {
        "chat_id": "-1001213886944",
        "text": f"{message}"
    }
    response = requests.post(url, json=data)
    return jsonify(response.json())

@app.route("/offerte_lavoro")
def offerte_lavoro():
    url = "https://api.airtable.com/v0/app371e6RlBMnvOa0/Bartender_Annunci?maxRecords=10&sort%5B0%5D%5Bfield%5D=Created&sort%5B0%5D%5Bdirection%5D=desc"
    headers = {
        "Authorization": f"Bearer {AirtableAPIKey}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    annunci = []

    for offerte in data["records"]:
        fields = offerte["fields"]
        zona = (f"Zona: " + fields.get("Zona", "N/A"))
        figura = (f"Figura ricercata: " + fields.get("Figura ricercata", "N/A"))
        singola_offerta = zona + " - " + figura
        annunci.append(singola_offerta)
    
    return jsonify(annunci)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
