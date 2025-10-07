import streamlit as st

def login():
    st.title("Validador de facturas 🧾")
    login = st.text_input("Introduce su nombre")
    password = st.text_input("Introduce su contraseña", type='password')

    st.button("Entrar")

    if st.button("Crear usuario"):
        st.session_state.page = "create_user"
        st.rerun()