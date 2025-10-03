from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict


class ObservacaoBase(BaseModel):
    especie: str
    tipo: str
    localizacao: str
    data_hora: Optional[datetime] = None
    condicoes: Optional[Dict[str, float]] = None
    observador: str


class ObservacaoCreate(ObservacaoBase):
    pass 


class ObservacaoResponse(ObservacaoBase):
    id: int

    class Config:
        orm_mode = True

        