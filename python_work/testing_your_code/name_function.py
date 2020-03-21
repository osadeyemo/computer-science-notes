#testing a function

def get_formatted_name(first, last):
	"""Generate a neatly formatted full name."""
	full_name = f"{first} {last}"
	return full_name.title()

#testing a function
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
	first = input("\nPlease give me a first name: ")
	if first == 'q':
		break
	last = input("Please give me a last name: ")
	if last == 'q':
		break

	formatted_name = get_formatted_name(first, last)
	print(f"\tNeatly formatted name: {formatted_name}.")

#a passing test
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""

	def test_first_last_name(self):
		"""Do names like 'janis Joplin' work?"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
	unittest.main()

#adding new tests
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'."""

	def test_first_last_name(self):
		"""Do names like 'janis Joplin' work?"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		"""Do names like 'Wolfgang Amadeus Mozart' work?"""
		formatted_name = get_formatted_name('wolfgang','mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
	unittest.main()
