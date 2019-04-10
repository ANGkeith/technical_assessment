FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB dathena

COPY ./requirements.txt /requirements.txt

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && apk add postgresql-client\
    && pip install -r  /requirements.txt\
    && apk del build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D dathena
USER dathena

