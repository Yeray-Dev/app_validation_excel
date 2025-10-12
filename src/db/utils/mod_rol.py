import streamlit as st
from db.database import SessionLocal
from db.models import User
from modules.utils.b_save import save_changes

ROLES = {
    "Usuario": 0,
    "Editor": 1,
    "Admin": 2,
    "Super Admin": 3
}

def mod_rol():
    db = SessionLocal()
    usuarios = db.query(User).all()
    db.close()

    opciones = {u.nombre: u.id for u in usuarios}
    usuario_seleccionado = st.selectbox(
        "Seleccione a un usuario",
        options=list(opciones.keys())
    )
    usuario_id = opciones[usuario_seleccionado]

    rol_actual = next((u.nivel for u in usuarios if u.id == usuario_id), None)
    rol_actual_nombre = next((name for name, val in ROLES.items() if val == rol_actual), None)

    rol_nuevo_nombre = st.selectbox(
        "Selecciona un nuevo rol",
        options=list(ROLES.keys()),
        index=list(ROLES.keys()).index(rol_actual_nombre) if rol_actual_nombre in ROLES else 0
    )

    rol_nuevo_valor = ROLES[rol_nuevo_nombre]
    if st.button("Guardar Cambios"):
        db = SessionLocal()
        user = db.query(User).filter(User.id == usuario_id).first()
        if user:
            user.nivel = rol_nuevo_valor
            db.commit()
            st.success(f"Rol de {user.nombre} has sido actualizado con exito.")
        else:
            st.error("No se ha encontrado usuario.")
        db.close()
    st.write(f"Usuario: {usuario_seleccionado} | Nuevo rol: {rol_nuevo_nombre} ({rol_nuevo_valor})")