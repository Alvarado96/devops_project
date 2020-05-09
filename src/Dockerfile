FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 

COPY main.py .
COPY database.py .
COPY status_codes.py .
COPY utils.py .
COPY static/swagger.yaml
