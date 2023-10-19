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

# Verifica as credenciais quando o botão de login é pressionado
if st.link_button("Login","https://material-apoio-campo-b2b-spi.streamlit.app/"):
    if user_input == username and password_input == senha_correta:
        st.success("Login bem-sucedido!")
        st.write("Bem-vindo, " + username)
    else:
        st.error("Credenciais inválidas. Tente novamente.")
        # Adicione aqui o código para a parte protegida da página após o login
        
