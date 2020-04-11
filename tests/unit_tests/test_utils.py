import unittest
import sys
sys.path.append('../../src/')
import utils

class TestUtilFunctions(unittest.TestCase):
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

	
	def test_has_missing_property_data(self):
		# values don't matter in this test
		no_missing_data = {'address':'a','city':'c','state':'s','zip':'z'}
		self.assertEqual(utils.has_missing_property_data(no_missing_data), '')

		err_msgs = ['missing address', 'missing city', 
		            'missing state', 'missing zip',
								'missing address missing city missing state missing zip']
		test_data = [
			{'city':'c', 'state':'s', 'zip':'z'},     # missing address
			{'address':'a', 'state':'s', 'zip':'z'},  # missing city
			{'address':'a', 'city':'c', 'zip':'z'},   # missing state
			{'address':'a', 'city':'c', 'state':'s'}, # missing zip
			{},                                       # missing everything
		]

		for (i,data) in enumerate(test_data):
			err_msg = utils.has_missing_property_data(data)
			self.assertEqual(err_msg, err_msgs[i])

	def test_has_invalid_address_length(self):
		valid_address = "a"
		self.assertFalse(utils.has_invalid_address_length(valid_address))

		no_address = ''
		self.assertTrue(utils.has_invalid_address_length(no_address))

		invalid_address = 'a' * 300
		self.assertTrue(utils.has_invalid_address_length(invalid_address))

	def test_has_invalid_city_length(self):
		valid_city = "San Antonio"
		self.assertFalse(utils.has_invalid_city_length(valid_city))

		no_city = ''
		self.assertTrue(utils.has_invalid_city_length(no_city))
		
		invalid_city = 'a' * 52
		self.assertTrue(utils.has_invalid_city_length(invalid_city))


if __name__ == '__main__':
	unittest.main()
