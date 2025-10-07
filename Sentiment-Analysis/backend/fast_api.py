from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, conint
from api_client import get_feedback_from_openai
from mongodb import MongoDBConnection
from config import DATABASE_NAME
from kafka_producer import KafkaFeedbackProducer
from bson import ObjectId
from typing import List, Dict, Optional
from auth.auth import create_access_token, verify_token
from validators.decorators import validate_comment_body
import os


MOCK_USER = "admin"
MOCK_PASSWORD = "1234"

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://mongo:27017/')


app = FastAPI(
    title="FastAPI",
    description="API para envio e análise de feedbacks.",
    version="0.1.0"
)

producer = KafkaFeedbackProducer()


class Evaluation(BaseModel):
    comment: str
    rating: int 


class Feedback(BaseModel):
    id: str
    comment: str
    rating: int
    descricao: Optional[str] = None
    status: Optional[str] = None


class LoginSchema(BaseModel):
    username: str
    password: str


mongo_conn = MongoDBConnection(MONGO_URI, DATABASE_NAME)
db = mongo_conn.get_database()


@app.get("/")
def root():
    return {"message": "Backend rodando."}


@app.post("/login")
def login(data: LoginSchema):
    if data.username == MOCK_USER and data.password == MOCK_PASSWORD:
        token = create_access_token({"sub": data.username})
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")


@app.get("/protegida/")
def rota_protegida(username: str = Depends(verify_token)):
    return {"message": f"Olá, {username}. Você está autenticado."}


@app.post("/feedback/")
async def feedback(
    evaluation: Evaluation,
    _: dict = Depends(validate_comment_body)
):
    producer.produce_feedback(evaluation.dict())
    return {
        "status": "Enviado para o tópico kafka", 
        "descricao": "Aguardando processamento"
    }


@app.get("/feedbacks/", response_model=List[Feedback])
async def get_feedback():
    feedback_collection = db["feedback"]
    feedbacks = feedback_collection.find().sort("_id", -1).limit(10)
    feedback_list = []

    for feedback in feedbacks:
        feedback_list.append({
            "id": str(feedback["_id"]),
            "comment": feedback["comment"],
            "rating": feedback["rating"],
            "descricao": feedback["descricao"],
            "status": feedback["status"]
        })

    return feedback_list

   