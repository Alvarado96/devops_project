import sqlite3
import sys

DATABASE = './properties.db'

# method used to handle inserting a new query entry
def insert_property(new_property):
	con = None
	statement = 'INSERT INTO properties(address, state, city, zip) VALUES(?,?, ?,?)'
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


# method returns an entry specified by the id in dictionary form
def select_property(property_id):
	con = None
	statement = 'SELECT * FROM properties WHERE id=?'
	try:
		con = establish_connection()
		cur = con.cursor()
		cur.execute(statement, property_id)
		row = cur.fetchall()
		return _to_dict(cur, row)
	except sqlite3.Error as e:
		print('ERROR: select_property: DB error:', e)
	except Exception as e:
		print('ERROR: select_property: error:', e)
	finally:
		if con:
			con.close()
	return None


# method handles the query for getting all entries in the database
def select_all_properties():
	con = None
	statement = 'SELECT * FROM properties'
	try:
		con = establish_connection()
		cur = con.cursor()
		cur.execute(statement)
		rows = cur.fetchall()
		return _to_dict(cur, rows)
	except sqlite3.Error as e:
		print('ERROR: select_all_property: DB error:', e)
	except Exception as e:
		print('ERROR: select_all_property: error:', e)
	finally:
		if con:
			con.close()
	return None


# method handles the query for deleting an entry specified by the id
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


# method connects to the database file in sqlite3
def establish_connection():
	con = None
	try:
		con = sqlite3.connect(DATABASE)	
	except sqlite3.Error as e:
		print('ERROR: establish_connection:', e)
		sys.exit(1)
	return con


# converts database entry to dictionary
def _to_dict(cursor, rows):
	ls = []
	for row in rows:
		ls.append(_make_dicts(cursor, row))		
	return ls
	

# returns a list of dictionarys
def _make_dicts(cursor, row):
	return dict((cursor.description[idx][0], value)
				for idx, value in enumerate(row))
