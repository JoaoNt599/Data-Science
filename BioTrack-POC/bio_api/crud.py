from sqlalchemy.orm import Session
from . import models, schemas


def get_observacoes(db: Session):
    return db.query(models.Observacao).all()

def get_observacao(db: Session, observacao_id: int):
    return db.query(models.Observacao).filter(models.Observacao.id == observacao_id).first()

def create_observacao(db: Session, observacao: schemas.ObservacaoCreate):
    db_observacao = models.Observacao(**observacao.dict())
    db.add(db_observacao)
    db.commit()
    db.refresh(db_observacao)
    return db_observacao