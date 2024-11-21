FROM cluster-base

RUN mkdir /opt/app
RUN mkdir /opt/logs && chmod 777 /opt/logs

ADD ./app /opt/app

RUN apt-get update -y
RUN pip install -r /opt/app/requirements.txt

WORKDIR ${SHARED_WORKSPACE}

EXPOSE 3000
CMD sh /opt/app/app-start.sh
