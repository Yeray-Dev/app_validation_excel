import streamlit as st
import pandas as pd
import db.permissions as pm
from db.database import SessionLocal
from db.models import Factura, User
from db.crear_facturas import crear_factura
from st_aggrid import  AgGrid, GridOptionsBuilder
from sqlalchemy.inspection import inspect
from db.crear_facturas import ver_facturas


def main_app():
    st.title("Validacion de Facturas")
    user = st.session_state.user
    user_rol = user["rol"]
    user_id = user["id"]
    if pm.can_upload_excel(user_rol):
        upload_file = st.file_uploader("Selecciona tu archivo Excel", type=["xlsx", "xls"])
        if upload_file:
            df = pd.read_excel(upload_file)        
            gb = GridOptionsBuilder.from_dataframe(df)
            gb.configure_pagination(paginationAutoPageSize=True)
            gb.configure_default_column(editable=False)
            gb.configure_column("nombre", cellStyle="color : black")
            grid_options = gb.build()
            AgGrid(
                df,
                gridOptions=grid_options,
                # fit_columns_on_grid_load = True,
                height=400,
            )
            if st.button("Guardar factura"):
                crear_factura(df, user_id)
    if pm.can_view_own(user_rol):
        def list_invoices(user_id):
            db = SessionLocal()
            invoices = db.query(Factura).filter(Factura.usuario_id == user_id).all()
            db.close()
            columnas_modelo = [c.key for c in inspect(Factura).mapper.column_attrs]
            data = []
            for f in invoices:
                row = {col: getattr(f, col) for col in columnas_modelo}
                data.append(row)

            df = pd.DataFrame(data)
            for col in df.columns:
                df[col] = df[col].apply(lambda x: str(x) if x is not None else "")

            return df
        df = list_invoices(user_id)
        for col in df.columns:
            df[col] = df[col].apply(lambda x: str(x) if x is not None else "")

        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_pagination(paginationAutoPageSize=True)
        gb.configure_default_column(editable=False)
        for col in df.columns:
            gb.configure_column(col, minWidth=120) 
        grid_options = gb.build()
        AgGrid(
            df,
            gridOptions=grid_options,
            height=400,
        )