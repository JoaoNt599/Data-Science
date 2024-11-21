#!/usr/bin/env bash

echo "=============================================================================================================="
echo "CRIANDO DATASET PARA ANÁLISE DE SENTIMENTO"
mkdir -p /opt/workspace/output
python /opt/workspace/scripts/create_sentiment_analyser_dataset.py >> /opt/logs/create_sentiment_analyser_dataset.log 2>&1

echo "=============================================================================================================="
echo "INICIALIZANDO O STREAMING DE DADOS DO REDDIT USANDO O SPARK STREAMING"
nohup python /opt/workspace/scripts/reddit_stream.py >> /opt/logs/reddit_stream.log 2>&1 &

echo "=============================================================================================================="
echo "INICIALIZANDO A APLICAÇÃO WEB"
export FLASK_APP=/opt/app/flaskr
export FLASK_RUN_PORT=3000
export FLASK_RUN_HOST=0.0.0.0
export FLASK_ENV=development
flask init-db
flask run