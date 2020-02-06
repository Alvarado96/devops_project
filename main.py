from flask import Flask, jsonify, request, render_template
import db as database
import sqlite3
from flask import g
from status_codes import Status
import database as db_sql
import json
DATABASE = './properties.db'

app = Flask(__name__)


@app.route('/properties', methods=['GET'])
def get_all_properties():
	res = []
	db = database.get_all()
	for id in db.keys():
		res.append({
			'id':id, 
			'address':db[id]['address'], 
			'zip':db[id]['zip'],
		})
	
	return jsonify(res)


@app.route('/properties/<int:id>', methods=['DELETE'])
def delete_property(id):
	if database.remove(id):
		return jsonify({'message':'deleted'})
	else:
		rsp = jsonify({'message':'error \'{}\' not found'.format(id)})
		return rsp, Status.NOT_FOUND.value


@app.route('/properties/<int:id>', methods=['GET'])
def get_id_properties(id):
	conn = db_sql.get_db()
	conn.row_factory = db_sql.dict_factory

	cursor = conn.cursor()
	cursor.execute("select * from properties where id=" + str(id))

	results = cursor.fetchall()
	return jsonify(results[0])
	conn.close()
	'''
	if database.get_by_id(id):
		return jsonify(database.get_by_id(id))
	else:
		rsp = jsonify({'message':'error \'{}\' not found'.format(id)})
		return rsp, Status.NOT_FOUND.value
	'''

@app.route('/properties', methods=['POST'])
def insert_property():
	errors = []
	req_data = request.get_json()

	address = req_data['address']
	city = req_data['city']
	state = req_data['state']
	zip_code = req_data['zip']

	if len(address) < 1 or len(address) > 200:
		errors.append({"message":"address is not between 1 and 200 characters"})

	if len(city) < 1 or len(city) > 50:
		errors.append({"message":"city is not between 1 and 50 characters"})

	if not len(state) == 2:
		errors.append({"message":"state is not exactly two characters"})

	if len(zip_code) < 5 or len(zip_code) > 10:
		errors.append({"message":"zip is not between 5 and 10 characters"})

	if errors:
		return jsonify(errors), Status.BAD_REQUEST.value

	database.insert(len(database.db) + 1, address, city, state, zip_code)

	return jsonify([{"message":"added"}]), Status.CREATED.value


@app.route('/hello')
def hello():
	return jsonify([{"message":"hello yourself"}])


if __name__ == '__main__':
	app.run(debug=True)
