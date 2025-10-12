import streamlit as st
import pandas as pd
import db.permissions as pm
from db.database import SessionLocal
from db.models import Factura

def save_changes(updated_df):
    if st.button("Guardar Cambios"):
        db = SessionLocal()
        for _, row in updated_df.iterrows():
            factura = db.query(Factura).filter(Factura.id == row["id"]).first()
            if factura:
                factura.validacion = bool(row["validacion"])
                factura.estado_validacion = bool(row["estado_validacion"])
        db.commit()
        db.close()
        st.success("Base de datos actualizada.")