#!/usr/bin/env bash

SPARK_VERSION="3.2.0"
HADOOP_VERSION="3.2"
JUPYTERLAB_VERSION="3.2.4"

docker build \
  -f ./docker/cluster-base.Dockerfile \
  -t cluster-base .

docker build \
  --build-arg spark_version="${SPARK_VERSION}" \
  --build-arg hadoop_version="${HADOOP_VERSION}" \
  -f ./docker/spark-base.Dockerfile \
  -t spark-base .

docker build \
  -f ./docker/spark-master.Dockerfile \
  -t spark-master .

docker build \
  -f ./docker/spark-worker.Dockerfile \
  -t spark-worker .

docker build \
  --build-arg spark_version="${SPARK_VERSION}" \
  --build-arg jupyterlab_version="${JUPYTERLAB_VERSION}" \
  -f ./docker/jupyterlab.Dockerfile \
  -t jupyterlab .

docker build \
  -f ./docker/web-app.Dockerfile \
  -t web-app .