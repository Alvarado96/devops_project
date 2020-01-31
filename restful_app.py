from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello')
def hello():
	return jsonify([{"message":"hello yourself"}])

if __name__ == '__main__':
	app.run(debug=True)

	