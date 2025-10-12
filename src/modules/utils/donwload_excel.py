import io
import streamlit as st
import pandas as pd

def to_excel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as write:
        df.to_excel(write, index=False, sheet_name='Date')
    processed_data = output.getvalue()
    return processed_data

def option_donwload(df, admin):
    df_validados = df[df["validacion"] == True]
    df_no_validados = df[df["validacion"] == False]
    df_open = df[df["estado_validacion"] == False]
    df_close = df[df["estado_validacion"] == True]
    download_excel(df_validados, "Validados")
    download_excel(df_no_validados, "No Validados")
    if admin == True:
        download_excel(df_open, "Abiertos")
        download_excel(df_close, "Cerrados")
    download_excel(df, "Completo")

def download_excel(df, text):
    excel_data = to_excel(df)
    st.download_button(
            label = f"Descargar excel {text}",
            data = excel_data,
            file_name = f"Datos_filtrados_{text}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )