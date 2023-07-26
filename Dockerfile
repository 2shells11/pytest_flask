FROM python:3.6.1-alpine

WORKDIR /pytest

ADD . /pytest

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .


