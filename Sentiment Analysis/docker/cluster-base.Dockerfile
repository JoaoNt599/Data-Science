ARG debian_buster_image_tag=11-jre-slim
FROM openjdk:${debian_buster_image_tag}

ARG shared_workspace=/opt/workspace
ARG spark_version=3.2.0

RUN mkdir -p ${shared_workspace} && \
    apt-get update -y && \
    apt-get install -y python3 python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*

RUN pip install pyspark==${spark_version} && \
    pip install --user -U nltk && \
    pip install praw

RUN python -m nltk.downloader all

ENV SHARED_WORKSPACE=${shared_workspace}

VOLUME ${shared_workspace}
CMD ["bash"]