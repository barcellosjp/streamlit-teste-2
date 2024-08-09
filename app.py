import streamlit as st
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Configuração do Streamlit Secrets
secrets = st.secrets["gcp"]

# Definindo o escopo e autenticando
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(secrets, scope)
client = gspread.authorize(creds)

# Acessando a planilha
spreadsheet_url = "YOUR_SPREADSHEET_URL"
sheet = client.open_by_url(spreadsheet_url).sheet1

# Lendo os dados da planilha
data = sheet.get_all_records()

# Convertendo os dados para um DataFrame
df = pd.DataFrame(data)

# Exibindo o DataFrame no Streamlit
st.title('Dashboard do Google Sheets')
st.write(df)

# Edição de dados
st.subheader('Editar Dados')

# Seleção da linha a ser editada
row_index = st.number_input('Selecione o índice da linha para editar', min_value=0, max_value=len(df)-1, step=1)

# Exibindo os dados da linha selecionada
row_data = df.iloc[row_index]
st.write(f'Dados da linha {row_index}:', row_data)

# Campos de entrada para edição
columns = df.columns
edited_data = {}
for column in columns:
    new_value = st.text_input(f'Editar {column}', value=row_data[column])
    edited_data[column] = new_value

# Botão para salvar alterações
if st.button('Salvar Alterações'):
    # Atualizando os dados no DataFrame
    df.loc[row_index] = edited_data
    
    # Atualizando a planilha
    cell_list = sheet.range(f'A{row_index + 2}:Z{row_index + 2}')  # Ajuste o range conforme necessário
    for cell, (column, value) in zip(cell_list, edited_data.items()):
        cell.value = value
    sheet.update_cells(cell_list)

    st.success('Dados atualizados com sucesso!')
    st.write(df)
