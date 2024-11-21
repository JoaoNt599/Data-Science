FROM cluster-base

ARG jupyterlab_version=3.2.4

RUN apt-get update -y && \
    pip install wget jupyterlab==${jupyterlab_version}

EXPOSE 8888
WORKDIR ${SHARED_WORKSPACE}
CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=