FROM python:3.8-alpine

RUN mkdir /usr/src/app/
WORKDIR /usr/src/app
RUN mkdir storage

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app/* ./

CMD ["python3", "server.py"]
