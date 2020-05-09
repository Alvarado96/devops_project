from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'fgd806'
app.config['MYSQL_CURSORCLASSS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('''CREATE TABLE properties (id Integer Primary Key Not Null, 
        address VARCHAR(200) Not Null, city VARCHAR(50) Not Null, state VARCHAR(2) Not Null,
        zip VARCHAR(10) Not Null)''')
   
if __name__ == '__main__':
    app.run(debug=True)