from sqlalchemy import Column, Integer, String, Date, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    nivel = Column(String, default="User") #? User - Evaluator - Admin - SuAdmin

    facturas = relationship("Factura", back_populates="usuario")

class Factura(Base):
    __tablename__ = "facturas"

    id = Column(Integer, primary_key=True, index=True)
    n_factura = Column(String, nullable=False)
    fecha_Emision = Column(Integer, index=True)
    id_paciente = Column(Integer, nullable=False)
    nombre_paciente = Column(String, nullable=False)
    fecha_atencion = Column(Date, nullable=False)
    servicios = Column(String, nullable=False)
    codigo_procedimiento = Column(Integer, nullable=False)
    subtotal = Column(Float(10, 2), nullable=False)
    impuestos = Column(Float(10, 2), nullable=False)
    total = Column(Float(10, 2), nullable=False)
    metodo_pago = Column(String, nullable=False)
    estado_pago = Column(String, nullable=False)
    seguro = Column(String)
    poliza = Column(String)
    departamento = Column(String, nullable=False)
    medico = Column(String, nullable=False)
    notas = Column(String)
    validacion = Column(Boolean, default=False, nullable=False)
    estado_validacion = Column(Boolean, default=False, nullable=True)
    

    usuario_id = Column(Integer, ForeignKey("users.id"))
    usuario = relationship("User", back_populates="facturas")