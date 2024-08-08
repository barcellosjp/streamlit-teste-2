import pandas as pd
import os
import streamlit as st


id_planilha = '1UvAo5LKW2bZf7tKoxoG-BNXwee6KUIf7Iq70u9zpvjI'
# URL da planilha pública
url = f"https://docs.google.com/spreadsheets/d/{id_planilha}/export?format=csv"

# Ler a planilha diretamente em um DataFrame
df = pd.read_csv(url)

# Exibir os dados
print(df.head())  # Exibe as primeiras linhas da planilha

usuario = st.secrets('USERNAME_SECRETS')
print(usuario)

# Configurações iniciais
st.title('Meu App Seguro')
st.write("Aqui está um exemplo de gráfico:")

