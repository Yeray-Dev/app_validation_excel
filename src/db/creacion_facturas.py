import streamlit as st
from db.database import SessionLocal
from db.models import Factura
#! TESTING
def ver_facturas():
    db = SessionLocal()
    facturas = db.query(Factura).all()
    db.close()
    return facturas
#! END TESTING
def crear_factura(df):

    session = SessionLocal()
    success_counter = 0
    error_messages = []

    for index, row in df.iterrows():
        try:
            factura = Factura(**row.to_dict())

            session.add(factura)
            success_counter += 1
        except Exception as e:
            session.rollback()
            error_messages.append(f"Fila {index + 1}: Error de integridad - {str(e)}")
    try:
        session.commit()
        st.success(f"{success_counter} Facturas guardadas correctamente")
        if error_messages:
            st.warning("Algunsa filas no se guardaron:")
            for msg in error_messages:
                st.error(msg)
    except Exception as e:
        session.rollback()
        st.error(f"Error al guardar la bas de dastos: {str(e)}")
    finally:
        session.close()

