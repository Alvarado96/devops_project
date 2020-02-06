import sqlite3
from flask import Flask
from flask import g

DATABASE = './properties.db'

app = Flask(__name__) 

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

def make_dicts(cursor, row):
	return dict((cursor.description[idx][0], value)
				for idx, value in enumerate(row))

def query_db(query, args=(), one=False):
	cur = g.db.execute(query, args)
	rv = [dict((cur.description[idx][0], value)
				for idx, value in enumerate(row)) for row in cur.fetchall()]
	return (rv[0] if rv else None)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d