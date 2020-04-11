import unittest
import sys
sys.path.append('../../src/')
import utils

class TestUtilFunction(unittest.TestCase):
	def test_is_integer(self):
		for i in range(5):
			self.assertTrue(utils.is_integer(str(i)))

		self.assertFalse(utils.is_integer('not an integer'))
		self.assertFalse(utils.is_integer('3.145'))

	def test_has_invalid_or_missing_key(self):
		valid_key = {'Api-Key':'cs4783FTW'}
		self.assertFalse(utils.has_invalid_or_missing_key(valid_key))

		no_key = {'Not-here':'not-here'}
		self.assertTrue(utils.has_invalid_or_missing_key(no_key))

		wrong_key = {'Api-Key':'1234'}
		self.assertTrue(utils.has_invalid_or_missing_key(wrong_key))


if __name__ == '__main__':
	unittest.main()
