# Contains helper functions used in API endpoint functions

# Determines if the given ID is an integer or not
def is_integer(id):
	try:
		int(id)
		return True
	except ValueError:
		return False

	
# Determines if the given request contains the correct API key
def has_invalid_or_missing_key(headers):
	if 'Api-Key' not in headers:
		return True
	return headers['Api-Key'] != 'cs4783FTW'


# Determines if the request has any missing fields
def has_missing_property_data(req_data):
	error_msg = ""
	if 'address' not in req_data:
		error_msg += 'missing address '
	if 'city' not in req_data:
		error_msg += 'missing city '
	if 'state' not in req_data:
		error_msg += 'missing state '
	if 'zip' not in req_data:
		error_msg += 'missing zip '
	return error_msg.strip()

# Determines if the address length is correct length
def has_invalid_address_length(address):
	if len(address) > 200 or len(address) < 1:
		return True
	return False

# Determines if city length is correct length
def has_invalid_city_length(city):
	if len(city) < 1 or len(city) > 50:
		return True
	return False

# Determines if state length is correct length
def has_invalid_state_length(state):
	if len(state) != 2:
		return True
	return False

