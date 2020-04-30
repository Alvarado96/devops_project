from flask import Flask
from flask_mysqldb import MySQL
from flask import Blueprint
from main import app
import mysql.connector
import json
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

if not os.environ.get('MYSQL_DB'):
    print('No MySQL database name')
    sys.exit(1)

mydb = mysql.connector.connect(
  host=os.environ.get('MYSQL_HOST'),
  user=os.environ.get('MYSQL_USER'),
  passwd=os.environ.get('MYSQL_PASSWORD'),
  database=os.environ.get('MYSQL_DB')
)

def select_all_properties():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM properties")
    myresult = mycursor.fetchall()
    return _to_dict(mycursor, myresult)

# method used to handle inserting a new query entry
def insert_property(new_property):
    mycursor = mydb.cursor()
    statement = """INSERT INTO properties(address, state, city, zip) VALUES(%s,%s,%s,%s)"""
    row_cnt = mycursor.execute(statement, new_property)
    mydb.commit()
    return row_cnt

# method updates an entry in the database
def update_property(property_id, address, city, state, zip_code):
    mycursor = mydb.cursor()
    row_cnt = 1
    
    if address:
        statement = """UPDATE properties set address=%s where id=%s"""
        mycursor.execute(statement, (address, property_id,))
        row_cnt = mycursor.rowcount

    if city:
        statement = """UPDATE properties set city=%s where id=%s"""
        mycursor.execute(statement, (city, property_id,))
        row_cnt = mycursor.rowcount

    if state:
        statement = """UPDATE properties set state=%s where id=%s"""
        mycursor.execute(statement, (state, property_id,))
        row_cnt = mycursor.rowcount

    if zip_code:
        statement = """UPDATE properties set zip=%s where id=%s"""
        mycursor.execute(statement, (zip_code, property_id,))
        row_cnt = mycursor.rowcount

    mydb.commit()
    return str(row_cnt)

# method returns an entry specified by the id in dictionary form
def select_property(property_id):
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM properties where id = %s", (property_id,))

    myresult = mycursor.fetchall()

    return _to_dict(mycursor, myresult)

# method handles the query for deleting an entry specified by the id
def delete_property(property_id):
    mycursor = mydb.cursor()
    statement = """DELETE FROM properties WHERE id=%s"""
    row_cnt = mycursor.execute(statement, (property_id,))
    mydb.commit()
    return row_cnt

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
