from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database


# generate tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="BioTrack API", version="1.0")


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/observacoes/", response_model=schemas.ObservacaoResponse)
def create_observacao(observacao: schemas.ObservacaoCreate, db: Session = Depends(get_db)):
    return crud.create_observacao(db=db, observacao=observacao)

@app.get("/observacoes/", response_model=list[schemas.ObservacaoResponse])
def listar_observacoes(db: Session = Depends(get_db)):
    return crud.get_observacoes(db)

@app.get("/observacoes/{observacao_id}", response_model=schemas.ObservacaoResponse)
def get_observacao(observacao_id: int, db: Session = Depends(get_db)):
    db_observacao = crud.get_observacao(db, observacao_id=observacao_id)
    if not db_observacao:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_observacao