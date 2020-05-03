USE flask-db;

GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION;
FLUSH PRIVILEGES;

CREATE TABLE properties(
	id INT NOT NULL AUTO_INCREMENT,
	address VARCHAR(200) NOT NULL,
  city VARCHAR(50) NOT NULL,
  state VARCHAR(2) NOT NULL,
  zip VARCHAR(10) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO properties (address, city, state, zip) 
VALUES("1111 One St.", "City One", "TX", "11111");
INSERT INTO properties (address, city, state, zip)
VALUES("2222 Two St.", "City Two", "TX", "22222");
INSERT INTO properties (address, city, state, zip)
VALUES("3333 Three St.", "City Three", "TX", "33333");
INSERT INTO properties (address, city, state, zip)
VALUES("4444 Four St.", "City Four", "TX", "44444");
INSERT INTO properties (address, city, state, zip)
VALUES("5555 Five St.", "City Five", "TX", "55555");
INSERT INTO properties (address, city, state, zip)
VALUES("6666 Six St.", "City Six", "TX", "66666");
