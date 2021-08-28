FROM python:3
ENV PYTHONUNBUFFERED=1

RUN pip3 install pipenv

WORKDIR /app
COPY Pipfile.lock .
RUN pipenv install --ignore-pipfile

COPY . .