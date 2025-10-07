FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY .env .env

ENV PYTHONPATH=/app/backend

CMD ["uvicorn", "fast_api:app", "--host", "0.0.0.0", "--port", "8000"]