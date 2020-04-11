from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
import database as db_sql
import utils
from status_codes import OK, CREATED, BAD_REQUEST,  \
                         UNAUTHORIZED, NOT_FOUND,   \
												 SERVER_ERROR
import sys
import argparse

app = Flask(__name__)
CORS(app)

# swagger ui path
@app.route('/static/<path:path>')
def send_static(path):
	return send_from_directory('static', path)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
	SWAGGER_URL,
	API_URL,
	config={
		'app_name': "Devop Project"
	}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


# get_all_properties() returns all rows in the database in json form
@app.route('/properties', methods=['GET'])
def get_all_properties():
	rows = db_sql.select_all_properties()
	if not rows:
		return jsonify({'message':'not found'}), NOT_FOUND
	return jsonify(rows), OK


# delete_property(id) removes a row in the database specified by the id
@app.route('/properties/<string:id>', methods=['DELETE'])
def delete_property(id):
	if not utils.is_integer(id):
		return jsonify({'message':'id not an integer'}), BAD_REQUEST

	if utils.has_invalid_or_missing_key(request.headers):
		return jsonify({'message':'missing or invalid key'}), UNAUTHORIZED
	
	rows_affected = db_sql.delete_property(id)
	if rows_affected == -1:
		return jsonify({'message':'error'}), SERVER_ERROR
	elif rows_affected == 0:
		return jsonify({'message':'not found'}), NOT_FOUND
	return jsonify({'message':'deleted'}), OK


# get_id_properties(id) returns a row in json form specified by the id
@app.route('/properties/<string:id>', methods=['GET'])
def get_id_properties(id):
	if not utils.is_integer(id):
		return jsonify({'message':'id not an integer'}), BAD_REQUEST

	row = db_sql.select_property(id)
	if not row:
		return jsonify({'message':'not found'}), NOT_FOUND
	return jsonify(row[0]), OK

	
# insert_property() inserts a new entry into the database
@app.route('/properties', methods=['POST'])
def insert_property():
	if utils.has_invalid_or_missing_key(request.headers):
		return jsonify({'message':'missing or invalid key'}), UNAUTHORIZED

	data = request.get_json()
	err_msg = utils.has_missing_property_data(data)
	if err_msg:
		return jsonify({'message':err_msg}), BAD_REQUEST

	errors = []
	address = data['address']
	city = data['city']
	state = data['state']
	zip_code = data['zip']
	
	if utils.has_invalid_address_length(address):
		errors.append({"message":"address is not between 1 and 200 characters"})

	if len(city) < 1 or len(city) > 50:
		errors.append({"message":"city is not between 1 and 50 characters"})

	if not len(state) == 2:
		errors.append({"message":"state is not exactly two characters"})

	if len(zip_code) < 5 or len(zip_code) > 10:
		errors.append({"message":"zip is not between 5 and 10 characters"})

	if errors:
		return jsonify(errors), BAD_REQUEST

	rows_affected = db_sql.insert_property((address, state, city, zip_code))
	
	return jsonify([{"message":"added"}]), CREATED


# put_id(id) updates an entry in the database
@app.route('/properties/<string:id>', methods=['PUT'])
def put_id_properties(id):
	if not utils.is_integer(id):
		return jsonify({'message':'id not an integer'}), BAD_REQUEST

	if utils.has_invalid_or_missing_key(request.headers):
		return jsonify({'message':'missing or invalid key'}), UNAUTHORIZED

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
		return jsonify([{"message":"not found"}]), NOT_FOUND

	if row:
		return jsonify([{"message":"updated"}]), OK

	
# hello() function created for testing purposes
@app.route('/hello')
def hello():
	return jsonify([{"message":"hello yourself"}])


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Web service')
	parser.add_argument('-i', type=str, default='127.0.0.1', dest='host', 
						help='IP of service (default: localhost')
	parser.add_argument('-p', type=int, default=12185, dest='port', 
						help='Port of service (default: 12185)')
	parser.add_argument('-m', type=str, default='http', dest='mode', 
						choices=['http', 'https'],
						help='Protocal of service (default: http)')
	parser.add_argument('-c', type=str, default='certs/localcert.pem',
						dest='cert', help='Path to https certitficate')
	parser.add_argument('-k', type=str, default='certs/localkey.pem',
						dest='key', help='Path to https key')
	
	args = parser.parse_args()
	if args.mode == 'http':
		app.run(host=args.host, port=args.port, debug=False)
	else:
		app.run(ssl_context=(args.cert, args.key), 
				host=args.host, port=args.port, debug=False)
