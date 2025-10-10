import streamlit as st
import pandas as pd
import db.permissions as pm
from db.database import SessionLocal
# from db.models import Factura
from db.creacion_facturas import crear_factura
from st_aggrid import  AgGrid, GridOptionsBuilder

from db.creacion_facturas import ver_facturas


def main_app():
    st.title("Validacion de Facturas")
    user = st.session_state.user
    user_rol = user["rol"]
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
                fit_colums_on_grid_load = True,
                height=400,
            )
            if st.button("Guardar factura"):
                crear_factura(df)
    # elif pm.can_view_own: