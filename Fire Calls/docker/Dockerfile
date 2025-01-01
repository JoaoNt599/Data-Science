FROM python:3.10-buster

RUN apt-get update && apt-get install -y openjdk-11-jdk
RUN apt-get update && apt-get install -y g++
RUN apt-get update && apt-get install -y curl
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Instala o Rust e Cargo
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Configurar variáveis de ambiente para PySpark
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

# Instale as bibliotecas Python necessárias
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Definir diretório de trabalho
WORKDIR /app

# Copiar todo o projeto para o contêiner
COPY . /app

# Comando padrão (pode ser alterado pelo docker-compose)
CMD ["python3", "scripts/visualization.py"]
