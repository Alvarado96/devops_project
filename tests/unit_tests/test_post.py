import sys
from flask import json
import unittest
sys.path.append('../../src/')
from main import app

class FlaskTestCase(unittest.TestCase):
    def test_post_missing_key(self):
    	print("Testing POST test_post_missing_key")
    	tester = app.test_client(self)
    	info = {"address":"testing7", "city":"testing7", "state":"TX", "zip":"77777"}
    	response = tester.post('/properties', data=json.dumps(info))
    	self.assertEqual(response.status_code, 401)

    def test_address_length(self):
    	print("Testing address length")
    	address = "1" * 300
    	info = {"address":address, "city":"testing7", "state":"TX", "zip":"77777"}
    	tester = app.test_client(self)
    	header = {"Api-Key": "cs4783FTW"}
    	response = tester.post('/properties', json={"address":"testing7", "city":"testing7", "state":"TX", "zip":"77777"}, headers=header)
    	self.assertFalse(len(address) < 200)

    def test_created(self):
    	print("Testing property created")
    	info = {"address":"testing7", "city":"testing7", "state":"TX", "zip":"77777"}
    	tester = app.test_client(self)
    	header = {"Api-Key": "cs4783FTW"}
    	response = tester.post('/properties', json={"address":"testing7", "city":"testing7", "state":"TX", "zip":"77777"}, headers=header)
    	self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
	unittest.main()
