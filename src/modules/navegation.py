import streamlit as st
import pandas as pd
from db.database import SessionLocal
from db.models import Factura
from db.creacion_facturas import crear_factura
# from st_aggrid import  AgGrid, GridOptionsBuilder, GridUpdateMode

from db.creacion_facturas import ver_facturas

# def ver_facturas():
#     db = SessionLocal()
#     tabla = db.query(Factura).
#     db.close()
#     return tabla



def main_app():
    st.title("Validacion de Facturas")
    upload_file = st.file_uploader("Selecciona tu archivo Excel", type=["xlsx", "xls"])
    #! TESTING
    if st.button("Mostrar facturas abiertas"):
        vista_facturas = ver_facturas()
        for u in vista_facturas:
            st.write(f"{u.id} {u.n_factura} | {u.validacion} | {u.estado_validacion}")
    #! END TESTING
    if upload_file:
        df = pd.read_excel(upload_file)
        st.write("Vista previa del Excel")
        if st.button("Guardar factura"):
            crear_factura(df)
        st.dataframe(df)