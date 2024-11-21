### Requisitos

- Apache Spark 3.2.0 with Hadoop 3.2
- Python 3.8.10
- Pyspark 3.2.0
- Flask
- Docker e Docker Compose

### Criar cluster o spark e subir aplicação web

```shell
$ ./build-images.sh
$ docker-compose up -d
```

### Gerar secret

```shell
$ python -c 'import secrets; print(secrets.token_hex())'
```

### Spark Web
> http://localhost:8080

### Aplicação Web
> http://localhost:3000

### Jupyter Notebook
> http://localhost:8888