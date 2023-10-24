import streamlit as st
import pandas as pd
import time 
# Defina as credenciais de login
credenciais = {
    "GTD_B2B": "tecdados",
}

# Função de login
def login():
    st.subheader("Suporte Tecnico SPI Dados B2B")
    username = st.text_input("Nome de usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Login"):
        if username in credenciais and credenciais[username] == senha:
            return True
        else:
            st.error("Credenciais inválidas. Tente novamente.")
    return False

# Página protegida
def pagina_protegida():
    st.title("Suporte a campo SPI Dados B2B :sunglasses:")
    
    st.markdown(''' 
Formulários para gerar Scripts:
''')   
    st.link_button("SWT DATACOM DM-2104","https://colab.research.google.com/drive/14aiImv-qA5imtWNJoP9XXvUfuc4E1I0a?usp=sharing")
    st.link_button("ROTEADORES B2B", "https://colab.research.google.com/drive/1XXxemoXIcGC72XSWdW4pZd5AtgZYSx-H?usp=sharing")
    st.link_button("CONVERSORES_SIP_TDM","https://colab.research.google.com/drive/12yVdAx7O-g5K4H_UY5_RApN4o2AIzZ-F?usp=sharing")
    with st.container():
                 st.markdown(''' 
Firmware e IOS: :point_down:
''') 
    st.link_button("Repositórios IOS","https://drive.google.com/drive/folders/1lU9-1yEFGuEQIt5FtHuAM9VQjJXhhERY?usp=drive_link")

# Confwith st.sidebar:
    with st.sidebar:
    
        st.write("Materiais para Downloads")
        with st.spinner("Loading..."):
            time.sleep(3)
        st.link_button("Downloads", "https://drive.google.com/drive/folders/1dvHJka8s_3Pdtzif6ZLEgrG4pWBB46qn?usp=sharing")

# Verifique o estado de autenticação
is_authenticated = False

if "is_authenticated" in st.session_state:
    is_authenticated = st.session_state.is_authenticated

# Se o usuário está autenticado, mostre a página protegida
if is_authenticated:
    pagina_protegida()
else:
    is_authenticated = login()
    if is_authenticated:
        st.session_state.is_authenticated = True
        # Redirecione para a página protegida alterando os parâmetros da URL
        st.experimental_set_query_params(authenticated="true")
