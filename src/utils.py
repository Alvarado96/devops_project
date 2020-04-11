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
