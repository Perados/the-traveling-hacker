FROM python:3.6

ENV PYTHONBUFFERED 1

ADD requirements.txt /

RUN pip install -r /requirements.txt

RUN rm /requirements.txt

WORKDIR /the-traveling-hacker
