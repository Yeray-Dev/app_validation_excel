import streamlit as st
import pandas as pd
import db.permissions as pm
from db.database import SessionLocal
# from db.models import Factura
from db.creacion_facturas import crear_factura
# from st_aggrid import  AgGrid, GridOptionsBuilder

from db.creacion_facturas import ver_facturas


def main_app():
    st.title("Validacion de Facturas")
    user = st.session_state.user
    user_rol = user["rol"]
    if pm.can_upload_excel(user_rol):
        upload_file = st.file_uploader("Selecciona tu archivo Excel", type=["xlsx", "xls"])
        if upload_file:
            df = pd.read_excel(upload_file)
            st.write("Vista previa del Excel")
            if st.button("Guardar factura"):
                crear_factura(df)
    #! TESTING
    if st.button("Mostrar facturas abiertas"):
        vista_facturas = ver_facturas()
        for u in vista_facturas:
            st.write(f"{u.id} {u.n_factura} | {u.validacion} | {u.estado_validacion}")
    #! END TESTING
        # # st.dataframe(df)

        # # gb = GridOptionsBuilder.from_dataframe(df)
        # # gb.configure_pagination(paginationAutoPageSize=True)
        # # gb.configure_default_column(editable=False)
        # # grid_options = gb.build()

        # # AgGrid(
        # #     df,
        # #     gridOptions=grid_options,
        # #     fit_colums_on_grid_load = True,
        # #     theme='alpine',
        # #     height=400,
        # # )