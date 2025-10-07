from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import redis


SECRET_KEY = "secret_key" # recomendado: carregar usando uma env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

r = redis.Redis(host='redis', port=6379, decode_responses=True)

security = HTTPBearer()


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    session_key = f"session:{data['sub']}"
    r.setex(session_key, ACCESS_TOKEN_EXPIRE_MINUTES * 60, "active")

    return token


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY,  algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=403, detail="Token inválido")

        # Verifica se a sessão existe no Redis
        session_key = f"session:{username}"
        if not r.exists(session_key):
            raise HTTPException(status_code=401, detail="Sessão expirada ou inválida")
        
        return username

    except JWTError:
        raise HTTPException(status_code=403, detail="Token inválido")