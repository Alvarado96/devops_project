from flask import Flask
from flask_mysqldb import MySQL
from flask import Blueprint
from main import app
import os
import sys

# Check that database environment variables are set
if not os.environ.get('MYSQL_USER'):
    print('No MySQL user name')
    sys.exit(1)

if not os.environ.get('MYSQL_PASSWORD'):
    print('No MySQL password')
    sys.exit(1)

if not os.environ.get('MYSQL_HOST'):
    print('No MySQL hostname')
    sys.exit(1)

if not os.environ.get('MYSQL_DB')
    print('No MySQL database name')
    sys.exit(1)

app.config['MYSQL_USER'] = 'fgd806'
app.config['MYSQL_PASSWORD'] = 'Evlv3h7MzBF30ay967IS'
app.config['MYSQL_HOST'] = 'easel2.fulgentcorp.com'
app.config['MYSQL_DB'] = 'fgd806'
app.config['MYSQL_CURSORCLASSS'] = 'DictCursor'

mysql = MySQL(app)

# method handles the query for getting all entries in the database
def select_all_properties():
    cur = None
    statement = '''SELECT id FROM properties'''
    try:
        cur = mysql.connection.cursor()
        cur.execute(statement)
        rows = cur.fetchall()
        print(rows)
        return _to_dict(cur, rows)
    except Exception as e:
        print('ERROR: select_all_property: DB error:', e)
    except Exception as e:
        print('ERROR: select_all_property: error:', e)
    finally:
        if cur:
            cur.close()
    return None

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

# method updates an entry in the database
def update_property(property_id, address, city, state, zip_code):
    con = None
    row_cnt = 0
    con = establish_connection()
    cur = con.cursor()

    if address:
        statement = 'UPDATE properties set address=(?) where id=(?)'
        row_cnt = cur.execute(statement, (address, property_id)).rowcount

    if city:
        statement = 'UPDATE properties set city=(?) where id=(?)'
        row_cnt = cur.execute(statement, (city, property_id)).rowcount

    if state:
        statement = 'UPDATE properties set state=(?) where id=(?)'
        row_cnt = cur.execute(statement, (state, property_id)).rowcount

    if zip_code:
        statement = 'UPDATE properties set zip=(?) where id=(?)'
        row_cnt = cur.execute(statement, (zip_code, property_id)).rowcount

    con.commit()
    return row_cnt

# method returns an entry specified by the id in dictionary form
def select_property(property_id):
    con = None
    statement = 'SELECT * FROM properties WHERE id=?'
    try:
        con = establish_connection()
        cur = con.cursor()
        cur.execute(statement, (property_id,))
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

# converts database entry to dictionary
def _to_dict(cursor, rows):
    ls = []
    for row in rows:
        ls.append(_make_dicts(cursor, row))     
    return ls
    

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
