import streamlit as st
import getpass
import pandas as pd
import time 


# Define as credenciais de login
username = "GTD_B2B"
senha_correta = "tecdados"

# Configura o título da página
st.title("Suporte Técnico B2B SPI Dados")

# Define um fundo preto

# Cria campos de entrada de texto para o usuário e senha
user_input = st.text_input("Nome de usuário")
password_input = st.text_input("Senha", type="password")

# Verifica as credenciais quando o botão de login é pressionadost.link_button("Bem-vindo","https://material-apoio-campo-b2b-spi.streamlit.app/")
if st.button("Login"):
    if user_input == username and password_input == senha_correta:
        st.success("Bem Vindo, "  + username)
        st.link_button("Click para Acessar","https://material-apoio-campo-b2b-spi.streamlit.app/")
        
    else:
        st.error("Credenciais inválidas. Tente novamente.")
        # Adicione aqui o código para a parte protegida da página após o login
