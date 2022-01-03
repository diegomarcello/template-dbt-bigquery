FROM python:3.8-slim

RUN pip install --no-cache-dir apache-beam[gcp]==2.34.0
RUN pip install --no-cache-dir pytimeparse==1.1.8
RUN pip install --no-cache-dir pyyaml==5.4.1

RUN pip check

WORKDIR /usr/src/app

COPY . .

RUN apt update
RUN apt-get install -y wget
RUN apt-get install -y unzip

ENV GOOGLE_APPLICATION_CREDENTIALS /usr/src/app/credentials_edw.json

ENTRYPOINT [ "bash", "run.sh"]
