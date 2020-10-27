# Dockerfile
FROM python:3.7-stretch
RUN apt-get update -y
RUN apt-get install nano -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install libsndfile1 -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN ["mlchain", "run"]