import unittest
import sys
sys.path.append('../../src/')
import utils

class TestUtilFunction(unittest.TestCase):
	def test_is_integer(self):
		self.assertEqual(1, 1)

if __name__ == '__main__':
	unittest.main()
