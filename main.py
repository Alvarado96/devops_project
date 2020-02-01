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


@app.route('/hello')
def hello():
	return jsonify([{"message":"hello yourself"}])


if __name__ == '__main__':
	app.run(debug=True)
