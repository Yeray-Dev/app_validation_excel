import streamlit as st
from db.database import SessionLocal
from db.models import User, Factura
from db.utils.verify_user import verify_user
from modules.main import main_app
from st_aggrid import AgGrid, GridOptionsBuilder #! TESTING
import pandas as pd #! TESTING
from db.database import engine
from sqlalchemy import inspect

#! TESTING
def list_user():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users
def list_invoices():
    db = SessionLocal()
    invoice = db.query(Factura).all()
    db.close()
    return invoice

#! END TESTING

def login():
    st.title("Validador de facturas 🧾")
    login = st.text_input("Introduce su nombre")
    password = st.text_input("Introduce su contraseña", type='password')

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Entrar"):
            user = verify_user(login, password)
            if user:
                st.session_state.logged_in = True
                st.session_state.page = 'main'
                st.session_state.user = {
                    "id" : user.id,
                    "nombre" : user.nombre,
                    "rol" : user.nivel
                }
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
    if st.button("Ver facturas"):
        users = list_invoices()
        for u in users:
            st.write(f"{u.id} | {u.n_factura} {u.usuario_id}")
    #! END TESTING

