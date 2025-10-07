import streamlit as st
from db.database import SessionLocal
from db.models import User
from modules.login import login
import bcrypt

def creat_user(name, last_name, login, password):
    session = SessionLocal()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    new_user = User(
        nombre = name,
        apellidos = last_name,
        login = login,
        password = hashed_password.decode('utf-8')
    )

    session.add(new_user)
    session.commit()
    session.close()
    return True 


@st.dialog("Registro", dismissible = False)
def input_info():
    name = st.text_input("Name")
    last_name = st.text_input("Last Name")
    login = st.text_input("Login")
    password = st.text_input("Password", type="password")
    if st.button("Enviar"):
        if not all([name, last_name, login, password]):
            st.warning("Es obligatorio rellenar todos los campos.")
        else:
            if creat_user(name, last_name, login, password):
                st.write("Registro completo")
    if st.button("Atras"):
        st.session_state.page = 'login'
        st.rerun()
    
