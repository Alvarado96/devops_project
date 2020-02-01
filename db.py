# Code for the database interaction (when we have a DB)

# Replace this when we have the database setup
db = {
	1: {
		'address': '11 Dirt road street',
		'city': 'San Antonio',
		'state': 'Texas',
		'zip': '11111',
	},

	2: {
		'address': '22 Rock road street',
		'city': 'Austin',
		'state': 'Texas',
		'zip': '22222',
	},

	3: {
		'address': '33 Test Ave.',
		'city': 'Dallas',
		'state': 'Texas',
		'zip': '33333',
	},

	4: {
		'address': '444 Test road',
		'city': 'San Antonio',
		'state': 'Texas',
		'zip': '44444',
	},
}


def get_all():
	return db


def get_by_id(id):
	if id not in db:
		return 'ERROR: {} is not in the database'.format(id)
	
	return db[id]


def insert(id, address, city, state, zip_code):
	db[id] = {'address':address, 'city':city, 'state':state, 'zip':zip_code}
