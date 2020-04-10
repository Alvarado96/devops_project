import sys
import unittest
sys.path.append('../../')
from main import app

class FlaskTestCase(unittest.TestCase):
	def test_get_by_id(self):
		tester = app.test_client(self)
		response = tester.get('/properties/1')
		self.assertEqual(response.status_code, 200)

	def test_is_invalid_id(self):
		print("Testing invalid id  GET /properties/hello")
		tester = app.test_client(self)
		response = tester.get('/properties/hello')
		self.assertEqual(response.status_code, 400)

	def test_id_not_exist(self):
		print("Testing invalid id  GET /properties/50")
		tester = app.test_client(self)
		response = tester.get('/properties/50')
		self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
	unittest.main()