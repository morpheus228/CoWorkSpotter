FROM python:3.8-slim-buster
WORKDIR /code

# Upgrade installed packages
RUN apt-get -y update
RUN apt-get -y upgrade

# Install requirements
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
