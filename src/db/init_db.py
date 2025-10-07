from db.database import engine, Base
from db.models import User

Base.metadata.create_all(bind=engine)
print("Base de datos creada con exito")