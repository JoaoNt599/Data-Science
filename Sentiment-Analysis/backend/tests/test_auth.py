import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

import sys
import os
sys.path.append(os.path.dirname(__file__))
from api_client import get_feedback_from_openai

from backend.fast_api import app


client = TestClient(app)

@patch("backend.fast_api.authenticate_user")  
def test_login_sucesso(mock_auth):
    mock_auth.return_value = {"username": "admin"} 

    response = client.post("/login", json={"username": "admin", "password": "1234"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
