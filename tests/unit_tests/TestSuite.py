import unittest   
from test_get_by_id import FlaskTestCase
def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(FlaskTestCase())
    return test_suite

if __name__ == '__main__':
   suite = create_suite()

   runner=unittest.TextTestRunner()
   runner.run(suite)