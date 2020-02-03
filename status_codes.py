from enum import Enum

# Enum of HTTP status codes that will be used
class Status(Enum):
	OK = 200
	CREATED = 201
	BAD_REQUEST = 400
	NOT_FOUND = 404
	SERVER_ERROR = 500
