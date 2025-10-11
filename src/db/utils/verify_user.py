import streamlit as st
from db.database import SessionLocal
from db.models import User
import bcrypt

def verify_user(login, password):
    db = SessionLocal()
    user = db.query(User).filter_by(login = login).first()
    db.close()

    if not user:
        return False, "User incorrecto."
    
    if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return user
    else:
        return False, "Contraseña incorrecta."