from flask import Flask, jsonify, request
import database as db_sql
from status_codes import Status
import sys

app = Flask(__name__)

# get_all_properties() returns all rows in the database in json form
@app.route('/properties', methods=['GET'])
def get_all_properties():
	rows = db_sql.select_all_properties()
	if not rows:
		return jsonify({'message':'not found'}), Status.NOT_FOUND.value
	return jsonify(rows), Status.OK.value


# delete_property(id) removes a row in the database specified by the id
@app.route('/properties/<string:id>', methods=['DELETE'])
def delete_property(id):
	if not is_integer(id):
		return jsonify({'message':'id not an integer'}), Status.BAD_REQUEST.value

	if is_invalid_or_missing_key(request):
		return jsonify({'message':'missing or invalid key'}), Status.UNAUTHORIZED.value
	
	rows_affected = db_sql.delete_property(id)
	if rows_affected == -1:
		return jsonify({'message':'error'}), Status.SERVER_ERROR.value
	elif rows_affected == 0:
		return jsonify({'message':'not found'}), Status.NOT_FOUND.value
	return jsonify({'message':'deleted'}), Status.OK.value


# get_id_properties(id) returns a row in json form specified by the id
@app.route('/properties/<string:id>', methods=['GET'])
def get_id_properties(id):
	if not is_integer(id):
		return jsonify({'message':'id not an integer'}), Status.BAD_REQUEST.value

	row = db_sql.select_property(str(id))
	if not row:
		return jsonify({'message':'not found'}), Status.NOT_FOUND.value
	return jsonify(row[0]), Status.OK.value

	
# insert_property() inserts a new entry into the database
@app.route('/properties', methods=['POST'])
def insert_property():
	if is_invalid_or_missing_key(request):
		return jsonify({'message':'missing or invalid key'}), Status.UNAUTHORIZED.value

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


# put_id(id) updates an entry in the database
@app.route('/properties/<string:id>', methods=['PUT'])
def put_id_properties(id):
	if not is_integer(id):
		return jsonify({'message':'id not an integer'}), Status.BAD_REQUEST.value

	if is_invalid_or_missing_key(request):
		return jsonify({'message':'missing or invalid key'}), Status.UNAUTHORIZED.value

	req_data = request.get_json()
	address = ''
	city = ''
	state = ''
	zip_code = ''

	if req_data and 'address' in req_data:
		address = req_data['address']
	if req_data and 'city' in req_data:
		city = req_data['city']
	if req_data and 'state' in req_data:
		state = req_data['state']
	if req_data and 'zip' in req_data:
		zip_code = req_data['zip']

	row = db_sql.update_property(id, address, city, state, zip_code)

	if not row:
		return jsonify([{"message":"not found"}]), Status.NOT_FOUND.value

	if row:
		return jsonify([{"message":"updated"}]), Status.OK.value

	
# hello() function created for testing purposes
@app.route('/hello')
def hello():
	return jsonify([{"message":"hello yourself"}])


# Determines if the given ID is an integer or not
def is_integer(id):
	try:
		int(id)
		return True
	except ValueError:
		return False


# Determines if the given request contains the correct API key
def is_invalid_or_missing_key(req):
	if 'Api-Key' not in req.headers:
		return True

	return req.headers['Api-Key'] != 'cs4783FTW'


if __name__ == '__main__':
	mode = 'http'
	if len(sys.argv) > 2:
		print('Usage: %s [http/https]' % (sys.argv[0]))
		print('\tExample:\n\t$ python3 main.py https')
		sys.exit(1)

	if len(sys.argv) == 2:
		mode = sys.argv[1]
		if mode != 'http' and mode != 'https':
			print('ERROR: Invalid protocol: %s' % (mode))
			sys.exit(1)

	print('Using %s protocol...' % (mode))
	if mode == 'http':
		app.run(debug=False)	
	elif mode == 'https':
		print('https not supported yet')
