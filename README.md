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
* Response: \[{'id':id,'address':address,'city':city,'state':state,zip':zip}, ...\]

### /properties - POST
Adds a new property to the database
* Status Code: 201 or 400
* Response: {'message':'added'}

### /properties/\<id\> - GET
Gets a property with the specified id
* Status Code: 200 or 404
* Response: {'id':id,'address':address,'city':city,'state':state,zip':zip}

### /properties/\<id\> - DELETE
Deletes the property with the specified id
* Status Code: 200 or 404
* Response: {'message':'deleted'}

## Data Storage
To keep things as simple as possible we use sqlite3 to persist the data that our API handles.
Sqlite3 stores data in a single file (.db) which is stored in our repository. So all queries
made by the API are handled by that local database file.

## Running the Service
Need flask and sqlite3 installed, then just run:
```
$ python3 main.py
```
Server will be running at localhost:5000
