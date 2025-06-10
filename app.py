import streamlit as st
import pandas as pd
from agente import criar_agente
from dotenv import load_dotenv
import os

# Carrega variáveis do .env (se houver)
load_dotenv()

# Configuração da página
st.set_page_config(page_title="Agente Inteligente para Notas Fiscais", layout="wide")

# Cabeçalho com logo e título lado a lado
col1, col2 = st.columns([1, 10])
with col1:
    st.image("images/logo.jpg", width=130)
with col2:
    st.markdown(
        "<h1 style='display: flex; align-items: center; margin-bottom: 0;'>Agente Inteligente para Notas Fiscais</h1>",
        unsafe_allow_html=True
    )

# Mensagem inicial e exemplos de perguntas
st.markdown("""
### 🤖 Faça perguntas sobre as notas fiscais de janeiro de 2024!

**Exemplos de perguntas:**
- 🧾 Qual o valor total das notas fiscais?
- 📍 Quais estados mais emitiram notas?
- 👤 Quais os principais destinatários?
- 💬 (pressione Enter para enviar)*
""")

csv_path = "202401_NFs_Cabecalho.csv"

# Carrega o DataFrame caso precise usar em outras funções (mantém, mas não exibe)
df = pd.read_csv(csv_path, sep=';', encoding='utf-8', on_bad_lines='skip')
# st.dataframe(df.head())  # Exibe somente se quiser ver a tabela (deixe comentado)

try:
    # Cria o agente com acesso ao DataFrame
    agente = criar_agente(csv_path)
    pergunta = st.text_input("Pergunta", placeholder="Digite sua pergunta aqui...", label_visibility="collapsed")


    if pergunta:
        with st.spinner("🔎 Consultando os dados..."):
            resposta = agente.run(pergunta)
            st.markdown("### 📄 Resposta:")
            st.write(resposta)
except ValueError as e:
    st.error(str(e))
except Exception as ex:
    st.error(f"Ocorreu um erro inesperado: {ex}")
