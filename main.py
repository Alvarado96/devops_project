from flask import Flask, jsonify, request, render_template
import database as db_sql
from status_codes import Status

app = Flask(__name__)

@app.route('/properties', methods=['GET'])
def get_all_properties():
	rows = db_sql.select_all_properties()
	if not rows:
		return jsonify({'message':'not found'}), Status.NOT_FOUND.value
	return jsonify(rows), Status.OK.value

	
@app.route('/properties/<int:id>', methods=['DELETE'])
def delete_property(id):
	rows_affected = db_sql.delete_property(id)
	if rows_affected == -1:
		return jsonify({'message':'error'}), Status.SERVER_ERROR.value
	elif rows_affected == 0:
		return jsonify({'message':'not found'}), Status.NOT_FOUND.value
	return jsonify({'message':'deleted'}), Status.OK.value

	
@app.route('/properties/<int:id>', methods=['GET'])
def get_id_properties(id):
	row = db_sql.select_property(str(id))
	if not row:
		return jsonify({'message':'not found'}), Status.NOT_FOUND.value
	return jsonify(row), Status.OK.value
	'''
	conn = db_sql.get_db()
	conn.row_factory = db_sql.dict_factory

	cursor = conn.cursor()
	cursor.execute("select * from properties where id=" + str(id))

	results = cursor.fetchall()
	conn.close()
	return jsonify(results[0])
	'''
	

@app.route('/properties', methods=['POST'])
def insert_property():
	return jsonify({'message':'not supported'}), Status.NOT_FOUND.value
	'''
	conn = db_sql.get_db()
	
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

	params = (address, city, str('zip'))
	sql = 'insert into properties(address, city, zip) values(?,?,?)'
	cursor = conn.cursor()
	cursor.execute(sql, params) 
	conn.commit()
	conn.close()

	return jsonify([{"message":"added"}]), Status.CREATED.value
	'''


@app.route('/hello')
def hello():
	return jsonify([{"message":"hello yourself"}])


if __name__ == '__main__':
	app.run(debug=True)
