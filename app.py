import pandas as pd
import streamlit as st

# ID da planilha pública
id_planilha = '1UvAo5LKW2bZf7tKoxoG-BNXwee6KUIf7Iq70u9zpvjI'
# URL da planilha pública
url = f"https://docs.google.com/spreadsheets/d/{id_planilha}/export?format=csv"

# Ler a planilha diretamente em um DataFrame
df = pd.read_csv(url)

# Exibir os dados no Streamlit (em vez de print)
st.write(df.head())  # Exibe as primeiras linhas da planilha no app

# Acessar segredos
usuario = st.secrets['USERNAME_SECRETS']
# Exibir o segredo no Streamlit (apenas para testes; remova ou comente isso em produção)
st.write(f"Usuário: {usuario}")

# Configurações iniciais
st.title('Meu App Seguro')
st.write("Aqui está um exemplo de gráfico:")

# Exemplo de gráfico com os dados da planilha
st.line_chart(df)
