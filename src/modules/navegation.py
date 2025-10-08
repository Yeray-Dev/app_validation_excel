import streamlit as st
import pandas as pd
from db.database import SessionLocal
from db.models import Factura
from db.creacion_facturas import crear_factura
# from st_aggrid import  AgGrid, GridOptionsBuilder, GridUpdateMode


# def ver_facturas():
#     db = SessionLocal()
#     tabla = db.query(Factura).
#     db.close()
#     return tabla

def main_app():
    st.title("Validacion de Facturas")
    upload_file = st.file_uploader("Selecciona tu archivo Excel", type=["xlsx", "xls"])
    # if st.button("Mostrar facturas abiertas"):
    #     tablas = ver_facturas()
    if upload_file:
        df = pd.read_excel(upload_file)
        st.write("Vista previa del Excel")
        if st.button("Guardar factura"):
            crear_factura(df)
        st.dataframe(df)