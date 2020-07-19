FROM python:3.7-alpine
MAINTAINER Gyanendra Kumar Verma

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt



RUN mkdir /app
WORKDIR /app
COPY ./app /app

# creating a user for application so that root access is not given for image
RUN adduser -D user
USER user
