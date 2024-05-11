FROM python:3.11.8-slim as PYTHON_IMAGE

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /mnist/backend

RUN pip3 install --upgrade pip
COPY requirements.txt requirements.txt
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
RUN pip3 install -r requirements.txt


COPY . /mnist/backend/

EXPOSE 8000

