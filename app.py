from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Chiavi API e configurazioni
AirtableAPIKey = "patmwWf2nhxbqK0l4.ff8ce9c4a82d639ceda9bb3f690f1b8d8663a339dd25f0626b9011c02b7016e7"
TelegramToken = "8152616899:AAFdwcDFkiDoxzWz22ziGqhI70mR1EieHzo"
TelegramChatID = "-1001213886944"

@app.route("/")
def home():
    return "L'applicazione è finalmente in esecuzione!"

# Endpoint per inviare un messaggio manualmente
@app.route("/send_message/<message>")
def send_message(message):
    url = f"https://api.telegram.org/bot{TelegramToken}/sendMessage"
    data = {
        "chat_id": TelegramChatID,
        "text": f"{message}"
    }
    response = requests.post(url, json=data)
    return jsonify(response.json())

# Endpoint per ottenere offerte di lavoro
@app.route("/offerte_lavoro")
def offerte_lavoro():
    url = "https://api.airtable.com/v0/app371e6RlBMnvOa0/Bartender_Annunci?maxRecords=10&sort%5B0%5D%5Bfield%5D=Created&sort%5B0%5D%5Bdirection%5D=desc"
    headers = {
        "Authorization": f"Bearer {AirtableAPIKey}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    annunci = []

    for offerte in data.get("records", []):
        fields = offerte.get("fields", {})
        zona = f"Zona: {fields.get('Zona', 'N/A')}"
        figura = f"Figura ricercata: {fields.get('Figura ricercata', 'N/A')}"
        singola_offerta = zona + " - " + figura
        annunci.append(singola_offerta)
    
    return jsonify(annunci)

# Endpoint per gestire il webhook di Telegram
@app.route(f"/webhook/{TelegramToken}", methods=["POST"])
def webhook():
    data = request.get_json()

    # Aggiungi un log per debug
    print("Richiesta ricevuta:", data)

    # Controlla che il messaggio sia valido
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # Risponde al messaggio
        response_message = f"Hai inviato: {text}"
        url = f"https://api.telegram.org/bot{TelegramToken}/sendMessage"
        response = requests.post(url, json={
            "chat_id": chat_id,
            "text": response_message
        })
        print("Risposta Telegram:", response.json())

    return jsonify({"ok": True})

# Configurazione del webhook (da chiamare separatamente)
@app.route("/setup_webhook", methods=["GET"])
def setup_webhook():
    webhook_url = f"https://python-mnt5.onrender.com/webhook/{TelegramToken}"
    url = f"https://api.telegram.org/bot{TelegramToken}/setWebhook?url={webhook_url}"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
