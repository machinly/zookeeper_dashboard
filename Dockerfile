from python:2.7.15-jessie

COPY ./  /app/

WORKDIR /app

RUN pip install -r /app/requirements.txt 
