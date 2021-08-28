FROM python:3
ENV PYTHONUNBUFFERED=1
COPY . /code/
WORKDIR /code

RUN pip3 install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
