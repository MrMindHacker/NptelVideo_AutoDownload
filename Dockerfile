FROM python:3.6-alpine
MAINTAINER Keyur Sonar

ENV PYTHONUNBUFFERED 1
COPY ./requirement.txt /requirement.txt

RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

RUN pip install -r /requirement.txt

RUN mkdir /Auto_download
WORKDIR /Auto_download
COPY ./Auto_download /Auto_download

RUN adduser -D user
USER user
