import unittest
from city_functions import city_country

class NameTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""

	def test_city_country_name(self):
		"""Do names like 'lagos nigeria' work?"""
		formatted_city_and_country = city_country('lagos', 'nigeria')
		self.assertEqual(formatted_city_and_country, 'Lagos, Nigeria')

if __name__ == '__main__':
	unittest.main()