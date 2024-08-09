import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

# Configuração do Streamlit Secrets
secrets = st.secrets["gcp"]

# ID da planilha pública
id_planilha = '1UvAo5LKW2bZf7tKoxoG-BNXwee6KUIf7Iq70u9zpvjI'
# URL da planilha pública
url = f"https://docs.google.com/spreadsheets/d/{id_planilha}/export?format=csv"

# Defina o escopo e credenciais usando secrets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(
    {
        "type": "service_account",
        "project_id": st.secrets["google"]["project_id"],
        "private_key_id": st.secrets["google"]["private_key_id"],
        "private_key": st.secrets["google"]["private_key"].replace('\\n', '\n'),
        "client_email": st.secrets["google"]["client_email"],
        "client_id": st.secrets["google"]["client_id"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": st.secrets["google"]["client_x509_cert_url"]
    },
    scope
)

client = gspread.authorize(creds)

# Abra a planilha usando o ID ou URL
sheet = client.open_by_url(url).sheet1
data = sheet.get_all_records()

# Exiba os dados usando Streamlit
st.write(data)
