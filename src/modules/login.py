import streamlit as st
from db.database import SessionLocal
from db.models import User
from db.verify_user import verify_user
from modules.navegation import main_app

from db.database import engine
from sqlalchemy import inspect

#! TESTING
def list_user():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users
#! END TESTING

def login():
    st.title("Validador de facturas 🧾")
    login = st.text_input("Introduce su nombre")
    password = st.text_input("Introduce su contraseña", type='password')

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Entrar"):
            if verify_user(login, password):
                st.session_state.logged_in = True
                st.session_state.page = 'main'
                st.rerun()
                

    with col2:
        if st.button("Crear usuario"):
            st.session_state.page = "create_user"
            st.rerun()
    #! TESTING
    if st.button("Ver usuarios"):
        users = list_user()
        for u in users:
            st.write(f"{u.id} | {u.nombre} {u.apellidos} | {u.login} | {u.nivel}")
    #! END TESTING