import streamlit as st
from db.database import SessionLocal
from db.models import Factura, User
from datetime import date, datetime
import pandas as pd
#! TESTING
def ver_facturas():
    db = SessionLocal()
    facturas = db.query(Factura).all()
    db.close()
    return facturas
#! END TESTING
import streamlit as st
from db.database import SessionLocal
from db.models import Factura
from datetime import date, datetime
import pandas as pd

def crear_factura(df, user_id):
    session = SessionLocal()
    success_counter = 0
    error_messages = []

    columnas_validas = [
        "n_factura", "fecha_Emision", "id_paciente", "nombre_paciente",
        "fecha_atencion", "servicios", "codigo_procedimiento", "subtotal",
        "impuestos", "total", "metodo_pago", "estado_pago", "seguro",
        "poliza", "departamento", "medico", "notas", "validacion",
        "estado_validacion"
    ]

    df = df.loc[:, df.columns.isin(columnas_validas)].copy()
    df.reset_index(drop=True, inplace=True)

    def convertir_fecha(valor):
        if pd.isna(valor):
            return None
        if isinstance(valor, (date, datetime)):
            return valor if isinstance(valor, date) else valor.date()
        try:
            return pd.to_datetime(valor).date()
        except Exception:
            return None

    if "fecha_Emision" in df.columns:
        df["fecha_Emision"] = df["fecha_Emision"].apply(
            lambda x: int(x) if pd.notna(x) and str(x).isdigit() else None
        )
    if "fecha_atencion" in df.columns:
        df["fecha_atencion"] = df["fecha_atencion"].apply(convertir_fecha)

    for index, row in df.iterrows():
        try:
            data = row.to_dict()

            for col in ["subtotal", "impuestos", "total"]:
                if col in data and pd.notna(data[col]):
                    data[col] = float(data[col])
                else:
                    data[col] = None

            for col in ["id_paciente", "codigo_procedimiento"]:
                if col in data and pd.notna(data[col]):
                    data[col] = int(data[col])
                else:
                    data[col] = None

            for col in ["validacion", "estado_validacion"]:
                if col in data and pd.notna(data[col]):
                    data[col] = bool(data[col])
                else:
                    data[col] = False

            data["usuario_id"] = user_id

            factura = Factura(**data)
            session.add(factura)
            success_counter += 1

        except Exception as e:
            session.rollback()
            error_messages.append(f"Fila {index + 1}: Error de integridad - {str(e)}")

    try:
        session.commit()
        st.success(f"{success_counter} Facturas guardadas correctamente")
        if error_messages:
            st.warning("Algunas filas no se guardaron:")
            for msg in error_messages:
                st.error(msg)
    except Exception as e:
        session.rollback()
        st.error(f"Error al guardar la base de datos: {str(e)}")
    finally:
        session.close()
