import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Configuração do Streamlit Secrets
secrets = st.secrets["gcp"]

# Definindo o escopo e autenticando
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(secrets, scope)
client = gspread.authorize(creds)

# Acessando a planilha
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1TmNwXyHLChMKoDMmjdWGGyOAT4jfPq85s8Q8aWMaY3c/export?format=csv"
sheet = client.open_by_url(spreadsheet_url).sheet1

# Lendo os dados da planilha
data = sheet.get_all_records()

# Convertendo os dados para um DataFrame
df = pd.DataFrame(data)

# Exibindo o DataFrame no Streamlit
st.title('Dashboard do Google Sheets')
st.write(df)
