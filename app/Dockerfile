# syntax=docker/dockerfile:1
FROM python:3

RUN pip3 install pipenv

WORKDIR /app
COPY Pipfile.lock .
RUN pipenv install --ignore-pipfile

COPY . .