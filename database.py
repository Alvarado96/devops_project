import sqlite3
import sys

DATABASE = './properties.db'

def insert_property(new_property):
	con = None
	statement = 'INSERT INTO properties VALUES(?,?,?)'
	try:
		con = establish_connection()
		cur = con.cursor()
		row_cnt = cur.execute(statement, new_property).rowcount
		con.commit()
		return row_cnt
	except sqlite3.Error as e:
		print('ERROR: insert_property: DB error:', e)
	except Exception as e:
		print('ERROR: insert_property: other error:', e)
	finally:
		if con:
			con.close()
	return -1


def select_property(property_id):
	con = None
	statement = 'SELECT * FROM properties WHERE id=?'
	try:
		con = establish_connection()
		cur = con.cursor()
		cur.execute(statement, property_id)
		row = cur.fetchall()
		return row
	except sqlite3.Error as e:
		print('ERROR: select_property: DB error:', e)
	except Exception as e:
		print('ERROR: select_property: error:', e)
	finally:
		if con:
			con.close()
	return None


def select_all_properties():
	con = None
	statement = 'SELECT * FROM properties'
	try:
		con = establish_connection()
		cur = con.cursor()
		cur.execute(statement)
		rows = cur.fetchall()
		return rows
	except sqlite3.Error as e:
		print('ERROR: select_all_property: DB error:', e)
	except Exception as e:
		print('ERROR: select_all_property: error:', e)
	finally:
		if con:
			con.close()
	return None


def delete_property(property_id):
	con = None
	statement = 'DELETE FROM properties WHERE id=?'
	try:
		con = establish_connection()
		cur = con.cursor()
		row_cnt = cur.execute(statement, (property_id,)).rowcount
		con.commit()
		return row_cnt
	except sqlite3.Error as e:
		print('ERROR: delete_property: DB error:', e)
	except Exception as e:
		print('ERROR: delete_property: error:', e)
	finally:
		if con:
			con.close()
	return -1


def establish_connection():
	con = None
	try:
		con = sqlite3.connect(DATABASE)	
	except sqlite3.Error as e:
		print('ERROR: establish_connection:', e)
		sys.exit(1)
	return con


'''
def to_dict(cursor, row):
	d = {}
	for row in rows:
		for idx, col in enumerate(cursor.description):
			d[[col[0]] = row[idx]
	return d

    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
'''

'''
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
'''
