from db.database import SessionLocal
from db.models import User
import bcrypt

# Abrimos sesión
db = SessionLocal()

# Buscamos el usuario por login o id
user = db.query(User).filter_by(login="SuAdmin").first()

if user:
    # Le damos el nivel máximo (ejemplo: 'admin')
    user.nivel = 3
    
    # Si quieres también cambiar contraseña, opcional
    # user.password = bcrypt.hashpw("nueva_contraseña".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    db.commit()
    print(f"Usuario {user.login} actualizado a nivel {user.nivel}")
else:
    print("Usuario no encontrado")

db.close()
