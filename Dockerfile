FROM python:3.9

RUN apt-get update -y

WORKDIR /demo-temp

COPY ./requirements.txt /demo-temp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /demo-temp/requirements.txt

COPY ./app /demo-temp/app