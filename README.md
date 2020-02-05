# CS4783 Properties Web Service

## What was used?
* Python3
* Flask
* Sqlite3

## API Endpoints
### /hello - GET
* Status Code: 200
* Response: {'message':'hello yourself'}

### /properties - GET
Returns a list of all properties
* Status Code: 200
* Response: \[{'id':id,'address':address,'zip':zip}, ...\]

### /properties - POST
Adds a new property to the database
* Status Code:
* Response: {'message':'added'}

### /properties/\<id\> - GET
Gets a property with the specified id
* Status Code: 200 or 404
* Response: {'id':id,'address':address,'zip':zip}

### /properties/\<id\> - DELETE
Deletes the property with the specified id
* Status Code: 200 or 404
* Response: {'message':'deleted'}

## Data Storage
To keep things as simple as possible we use sqlite3 to persist the data that our API handles.
Sqlite3 stores data in a single file (.db) which is stored in our repository. So all queries
made by the API are handled by that local database file.

## Running the Service
