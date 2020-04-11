import sys
import unittest
sys.path.append('../../src/')
from main import app

class FlaskTestCase(unittest.TestCase):
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/properties')
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
	unittest.main()
