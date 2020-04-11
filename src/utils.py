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
