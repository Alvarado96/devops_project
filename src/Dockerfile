FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt 
RUN mkdir -p static
COPY main.py .
COPY status_codes.py .
COPY utils.py .

COPY static/swagger.yaml ./static
