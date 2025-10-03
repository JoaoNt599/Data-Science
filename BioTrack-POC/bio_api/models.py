
from sqlalchemy import Column, Integer, String, DateTime, JSON
from .database import Base
import datetime


class Observacao(Base):
    __tablename__ = "observacoes"

    id = Column(Integer, primary_key=True, index=True)
    especie = Column(String, index=True)
    tipo = Column(String) # animal, plant, insect
    localizacao = Column(String)
    data_hora = Column(DateTime, default=datetime.datetime.utcnow)
    condicoes = Column(JSON) # {"temperature": 22, "humidity": 80}
    observador = Column(String)