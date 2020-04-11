import sys
import json
import unittest
sys.path.append('../../src/')
from main import app

class TestAnalytics(unittest.TestCase):
    def test_post_missing_key(self):
    	print("Testing POST test_post_missing_key")
    	tester = app.test_client(self)
    	info = {"address":"testing7", "city":"testing7", "state":"TX", "zip":"77777"}
    	response = tester.post('/properties', data=json.dumps(info))
    	self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
	unittest.main()
