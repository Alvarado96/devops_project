import unittest
import sys
sys.path.append('../../src/')
import utils

class TestUtilFunction(unittest.TestCase):
	def test_is_integer(self):
		for i in range(5):
			self.assertTrue(utils.is_integer(str(i)))

		self.assertFalse(utils.is_integer("not an integer"))
		self.assertFalse(utils.is_integer("3.145"))

if __name__ == '__main__':
	unittest.main()
