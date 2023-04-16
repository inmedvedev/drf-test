FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install pipenv
RUN mkdir /app
COPY /Pipfile* /app/
WORKDIR /app
RUN pipenv install --system
COPY . /app/
RUN chmod +x entrypoint.sh