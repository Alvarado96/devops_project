FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 12185 
CMD ["python", "main.py"]

#FROM python:3.6

#EXPOSE 12185

#WORKDIR /app

#COPY requirements.txt /app
#RUN pip install -r requirements.txt

#COPY *.py /app
#COPY static/ /app

#CMD ["python", "/app/main.py"]
