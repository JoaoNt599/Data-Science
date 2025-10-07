import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.fast_api import app

client = TestClient(app)

headers = {"Authorization": "Bearer fake-token"}

def test_comentario_vazio():
    response = client.post(
        "/feedback/",
        json={"comment": "", "rating": 5},
        headers=headers
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Comentário não pode ser vazio."

def test_comentario_apenas_numeros():
    response = client.post(
        "/feedback/",
        json={"comment": "123456", "rating": 5},
        headers=headers
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Comentário não pode conter apenas números."

def test_comentario_valido():
    response = client.post(
        "/feedback/",
        json={"comment": "Excelente!", "rating": 5},
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["status"] == "Enviado para o tópico kafka"
