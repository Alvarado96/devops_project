<<<<<<< HEAD
From python:3.6

EXPOSE 12185

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY main.py /app
COPY database.py /app
COPY utils.py /app
COPY status_codes.py /app
CMD python3 -m pip install mysql-connector-python
CMD python main.py
=======
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt 

COPY main.py .
COPY database.py .
COPY status_codes.py .
COPY utils.py .
COPY static/swagger.yaml .
>>>>>>> e4290b8435ea4f4f497e7a16df02053d61706861
