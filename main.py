import os
import requests
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

ZAPI_INSTANCE_ID = "3F4FFA3F7F0A81865499FE1DAF8FDC00"
ZAPI_TOKEN = "2A71A3356451AFB0F55CFA6B"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

contatos = supabase.table("contatos").select("*").limit(3).execute().data

for contato in contatos:
    nome = contato["nome_contato"]
    telefone = contato["telefone"]
    mensagem = f"Olá, {nome} tudo bem com você?"

    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"

    dados = {
        "phone": telefone,
        "message": mensagem
    }

    resposta = requests.post(url, json=dados)

    print("Telefone:", telefone)
    print("Mensagem:", mensagem)
    print("Status:", resposta.status_code)
    print("Resposta:", resposta.text)
    print("-" * 30)