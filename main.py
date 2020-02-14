from flask import Flask, jsonify, request
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
	return jsonify(row[0]), Status.OK.value
	

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

	rows_affected = db_sql.insert_property((address, state, city, zip_code))
	
	return jsonify([{"message":"added"}]), Status.CREATED.value
	


@app.route('/hello')
def hello():
	return jsonify([{"message":"hello yourself"}])


if __name__ == '__main__':
	app.run(debug=True)
