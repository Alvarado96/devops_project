From python:3.6

EXPOSE 12185

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY main.py /app
COPY database.py /app
COPY utils.py /app
COPY status_codes.py /app
CMD python main.py
