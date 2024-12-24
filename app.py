## https://api.telegram.org/bot8152616899:AAFdwcDFkiDoxzWz22ziGqhI70mR1EieHzo/sendMessage

import requests

AirtableAPIKey = "patmwWf2nhxbqK0l4.ff8ce9c4a82d639ceda9bb3f690f1b8d8663a339dd25f0626b9011c02b7016e7"

def send_message(message):
  url = "https://api.telegram.org/bot8152616899:AAFdwcDFkiDoxzWz22ziGqhI70mR1EieHzo/sendMessage"
  header = {
  "content/type": "application/json"
  }
  data = {
  "chat_id": "-1001213886944",
  "text": f"{message}"
  }
  response = requests.post(url, json=data)
  print(response.json())

def offerte_lavoro():
  url = "https://api.airtable.com/v0/app371e6RlBMnvOa0/Bartender_Annunci?maxRecords=10&sort%5B0%5D%5Bfield%5D=Created&sort%5B0%5D%5Bdirection%5D=desc"
  headers = {
    "Authorization": "Bearer patmwWf2nhxbqK0l4.ff8ce9c4a82d639ceda9bb3f690f1b8d8663a339dd25f0626b9011c02b7016e7"
  }
  response = requests.get(url, headers=headers)
  data = response.json()
  annunci = []

  for offerte in data["records"]:
    fields = offerte["fields"]
    zona = (f"Zona: " + fields.get("Zona"))
    figura = (f"Figura ricercata: " + fields.get("Figura ricercata"))
    singola_offerta = zona + figura
    annunci.append(singola_offerta)
  for annuncio in annunci:
    prova(annuncio)


def prova(messaggio):
  url = "https://api.telegram.org/bot8152616899:AAFdwcDFkiDoxzWz22ziGqhI70mR1EieHzo/getUpdates"
  response = requests.get(url)
  chat_id = "chat_id" in response.json()
  url = "https://api.telegram.org/bot8152616899:AAFdwcDFkiDoxzWz22ziGqhI70mR1EieHzo/sendMessage"
  headers = {
    "content/type": "application/json"
  }
  data = {
    "chat_id": "-4697401047",
    "text": f"{messaggio}"
  }
  response = requests.post(url, data)
  print(response.json())

## azioni da intraprendere
offerte_lavoro()
