FROM mysql
ENV MYSQL_DATABASE flask-db
EXPOSE 3306
COPY . /docker-entrypoint-initdb.d/
