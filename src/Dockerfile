FROM python:3

WORKDIR /usr/src/app
RUN mkdir -p ./static
RUN chown -R root:root ./static
RUN chmod 777 ./static
COPY requirements.txt ./
RUN pip install -r requirements.txt 

COPY ./static/swagger.yaml ./static
RUN chmod 777 ./static/swagger.yaml
COPY main.py .
COPY status_codes.py .
COPY utils.py .
