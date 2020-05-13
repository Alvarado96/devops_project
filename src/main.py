from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
import utils
from status_codes import OK, CREATED, BAD_REQUEST,  \
                         UNAUTHORIZED, NOT_FOUND,   \
												 SERVER_ERROR
import sys
import argparse
import os
from pymongo import MongoClient
from bson.json_util import dumps
from bson import ObjectId

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


# Setup mongodb connection
client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
	27017
)

db = client.properties
db.properties.drop()
db.properties.insert_many([
  {
  "address": "410 E Huff",
  "city": "San Antonio",
  "state": "TX",
  "zip": "11111"
  },
  {
    "address": "21st Street",
  "city": "Houston",
  "state": "TX",
  "zip": "22222"
  }
])

# get_all_properties() returns all rows in the database in json form
@app.route('/properties', methods=['GET'])
def get_all_properties():
	props = db.properties.find()
	props = [prop for prop in props]
	return dumps(props), OK


# delete_property(id) removes a row in the database specified by the id
@app.route('/properties/<string:id>', methods=['DELETE'])
def delete_property(id):
	if utils.has_invalid_or_missing_key(request.headers):
		return jsonify({'message':'missing or invalid key'}), UNAUTHORIZED
	
	rows_affected = db.properties.delete_one({ "_id" : ObjectId(str(id))});
	if rows_affected == -1:
		return jsonify({'message':'error'}), SERVER_ERROR
	elif rows_affected == 0:
		return jsonify({'message':'not found'}), NOT_FOUND
	return jsonify({'message':'deleted'}), OK


# get_id_properties(id) returns a row in json form specified by the id
@app.route('/properties/<string:id>', methods=['GET'])
def get_id_properties(id):
	props = db.properties.find({"_id": ObjectId(str(id))})
	if not props:
		return jsonify({'message':'not found'}), NOT_FOUND
	props = [prop for prop in props]
	return dumps(props), OK
	

	
# insert_property() inserts a new entry into the database
@app.route('/properties', methods=['POST'])
def insert_property():
	if utils.has_invalid_or_missing_key(request.headers):
		return jsonify({'message':'missing or invalid key'}), UNAUTHORIZED

	data = request.get_json()
	err_msg = utils.has_missing_property_data(data)
	if err_msg:
		return jsonify({'message':err_msg}), BAD_REQUEST

	err_msg = ''
	address = data['address']
	city = data['city']
	state = data['state']
	zip_code = data['zip']

	if utils.has_invalid_address_length(address):
		err_msg += 'address is not between 1 and 200 characters '

	if utils.has_invalid_city_length(city):
		err_msg += 'city is not between 1 and 50 characters '

	if utils.has_invalid_state_length(state):
		err_msg += 'state is not exactly two characters '

	if utils.has_invalid_zip_length(zip_code):
		err_msg += 'zip is not between 5 and 10 characters'

	if err_msg:
		return jsonify({'message':err_msg.strip()}), BAD_REQUEST

	prop_doc = {
		'address': address,
		'state': state,
		'city': city,
		'zip': zip_code,
	}
	db.properties.insert_one(prop_doc)
	return jsonify([{'message':'added'}]), CREATED


# put_id(id) updates an entry in the database
@app.route('/properties/<string:id>', methods=['PUT'])
def put_id_properties(id):
	if utils.has_invalid_or_missing_key(request.headers):
		return jsonify({'message':'missing or invalid key'}), UNAUTHORIZED

	req_data = request.get_json()
	if not req_data:
		return jsonify({'message':'missing body'}), BAD_REQUEST

	address = ''
	city = ''
	state = ''
	zip_code = ''
	err_msg = ''

	if 'address' in req_data:
		address = req_data['address']
		if utils.has_invalid_address_length(address):
			err_msg += 'address is not between 1 and 200 characters '

	if 'city' in req_data:
		city = req_data['city']
		if utils.has_invalid_city_length(city):
			err_msg += 'city is not between 1 and 50 characters '

	if 'state' in req_data:
		state = req_data['state']
		if utils.has_invalid_state_length(state):
			err_msg += 'state is not exactly two characters '

	if 'zip' in req_data:
		zip_code = req_data['zip']
		if utils.has_invalid_zip_length(zip_code):
			err_msg += 'zip code is not between 5 and 10 characters '

	if err_msg:
		return jsonify({'message':err_msg.strip()}), BAD_REQUEST
    
	new_values = {"$set": {"address": address, "state": state, "city": city, "zip": zip_code}}
	#row = db_sql.update_property(id, address, city, state, zip_code)
	row = db.properties.update_one({"_id": ObjectId(str(id))},new_values)

	if not row:
		return jsonify([{"message":"not found"}]), NOT_FOUND

	return jsonify([{"message":"updated"}]), OK

	
# hello() function created for testing purposes
@app.route('/hello')
def hello():
	return jsonify([{"message":"hello yourself"}])


@app.route('/goodbye')
def goodbye():
	return jsonify([{'message':'goodbye yourself'}])


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Web service')
	parser.add_argument('-i', type=str, default='0.0.0.0', dest='host', 
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
