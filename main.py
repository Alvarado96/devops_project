from flask import Flask, jsonify, request
import db as database

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
		return jsonify({'message':'error \'{}\' not found'.format(id)})


@app.route('/properties/<int:id>', methods=['GET'])
def get_id_properties(id):
	if database.get_by_id(id):
		return jsonify(database.get_by_id(id))
	else:
		return jsonify({'message':'error \'{}\' not found'.format(id)}), 404


@app.route('/properties', methods=['POST'])
def insert_property():
	req_data = request.get_json()

	address = req_data['address']
	city = req_data['city']
	state = req_data['state']
	zip_code = req_data['zip']

	database.insert(len(database.db) + 1, address, city, state, zip_code)

	return jsonify([{"message":"added"}])


@app.route('/hello')
def hello():
	return jsonify([{"message":"hello yourself"}])


if __name__ == '__main__':
	app.run(debug=True)
