import streamlit as st
import pandas as pd
import db.permissions as pm
from db.database import SessionLocal
from db.models import Factura, User
from db.utils.crear_facturas import crear_factura, ver_facturas
from db.utils.mod_rol import mod_rol
from modules.utils.aggrid_config import render_aggrid
from modules.utils.b_save import save_changes
from modules.utils.donwload_excel import download_excel, option_donwload
import streamlit_js_eval
import streamlit.components.v1 as components
from sqlalchemy.inspection import inspect


def list_invoices(user_id, all = False):
    db = SessionLocal()
    query = db.query(Factura)
    if not all:
        query = query.filter(Factura.usuario_id == user_id)
    invoices = query.all()
    db.close()

    columnas_modelo = [c.key for c in inspect(Factura).mapper.column_attrs]
    data = [{col: getattr(f, col) for col in columnas_modelo} for f in invoices]
    return pd.DataFrame(data)

def main_app():
    st.title("Validacion de Facturas")
    user = st.session_state.user
    user_rol = user["rol"]
    user_id = user["id"]
    if pm.is_user(user_rol):
        upload_file = st.file_uploader("Selecciona tu archivo Excel", type=["xlsx", "xls"])
        if upload_file:
            df = pd.read_excel(upload_file)        
            render_aggrid(df)
            if st.button("subir factura"):
                crear_factura(df, user_id)
        df = list_invoices(user_id, False)
        df = df[df["estado_validacion"] == False]
        for col in df.columns:
            if col != "validacion" and col != "estado_validacion":
                df[col] = df[col].apply(lambda x: str(x) if x is not None else "")
        grid_responde = render_aggrid(df, editable_columns=["validacion"], hidden_columns=False)
        updated_df = grid_responde["data"]
        download_excel(updated_df, user["nombre"])
        save_changes(updated_df)

    if pm.is_evaluator(user_rol):
        df_full = list_invoices(user_id, True)
        df = df_full[(df_full["validacion"] == False) & (df_full["estado_validacion"] == False)]
        for col in df.columns:
            if col != "validacion" and col != "estado_validacion":
                df[col] = df[col].apply(lambda x: str(x) if x is not None else "")
        grid_responde = render_aggrid(df, editable_columns=["validacion"], hidden_columns=False)
        updated_df = grid_responde["data"]
        option_donwload(df_full, admin=False)
        save_changes(updated_df)

    if pm.is_admin(user_rol):
        df = list_invoices(user_id, True)
        for col in df.columns:
            if col != "validacion" and col != "estado_validacion":
                df[col] = df[col].apply(lambda x: str(x) if x is not None else "")
        grid_responde = render_aggrid(df, editable_columns=["validacion", "estado_validacion"], hidden_columns=False)
        updated_df = grid_responde["data"]
        option_donwload(df, admin=True)
        save_changes(updated_df)
    if pm.is_suadmin(user_rol):
        mod_rol()