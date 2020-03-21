#reading an entire file
with open('linux_commands.txt') as file_object:
	contents = file_object.read()
print(contents.rstrip()	)

#to look for files in another directory, = page 186
#with open('folder name/filename.txt') as file_object:

#absolute path file
#file_path = C:\\Users\\Labi\Desktop\\python_work\\files and exceptions
#with open(file_path) as file_object:

#reading line by line
filename = "linux_commands.txt"

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

#making a list of lines from a file
filename = "linux_commands.txt"

with open(filename) as file_object:
	lines = file_object.readlines()

	for line in lines:
		print(line.rstrip())

#working with a file's contents
filename = "pi_digits.txt"

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

#large files: One million digits
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

print(f'{pi_string[:52]}...')
print(len(pi_string))

#how to check if a word is in a file
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi!")

#writing to an empty file
filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.")

#writing multiple line
filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

#appending to file
filename = 'programming.txt'

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")

#Handling the ZeroDivisionError Exception = page 194 
#print(5/0)

try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

#using exceptions to prevent crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero!")
	else:
		print(answer)

#handling the filenotfounderror exception
filename = 'alice.txt'

try:
	with open(filename, encoding='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")

#analyzing text
filename = 'alice.txt'

try:
	with open(filename, encoding='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")
else:
	# Count the approximate number of words in the file.
	words = contents.split()
	num_words = len(words)
	print(f"The file {filename} has about {num_words} words.")

#working with one files
def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} does not exist.")
	else:
		# Count the approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words.")

filename = 'alice.txt'
count_words(filename)

#working with multiple files
def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} does not exist.")
	else:
		# Count the approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)

#failing silently
def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
		# Count the approximate number of words in the file.
		words = contents.split()
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)

#storing data
#using json() and json.load()

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
	json.dump(numbers, f)

#using json.load()
import json

filename = 'numbers.json'
with open(filename) as f:
	numbers = json.load(f)

print(numbers)

#saving and reading user-generated
#1
import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
	json.dump(username, f)
	print(f"We'll remember you when you come back, {username}!")

#2
import json

filename = 'username.json'

with open(filename) as f:
	username = json.load(f)
	print(f"Welcome back, {username}!")

#3
import json

#Load the username, if it has been stored previously.
#Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
	with open(filename) as f:
		username = json.load(f)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as f:
		json.dump(username, f)
		print(f"We'll remember you when you come back, {username}!")
else:
	print(f"Welcome back, {username}!")

#refactoring = is when you move a block of code into a function
import json

def greet_user():
	"""Greet the user by name."""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		username = input("What is your name? ")
		with open(filename, 'w') as f:
			json.dump(username, f)
			print(f"We'll remember you when you come back, {username}!")
	else:
		print(f"Welcome back, {username}!")

greet_user()

#
import json

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None 
	else:
		return username

def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}!")
	else:
		username = input("What is your name? ")
		filename = 'username.json'
		with open(filename, 'w') as f:
			json.dump(username, f)
			print(f"We'll remember you when you come back, {username}!")

greet_user()

#
import json

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None 
	else:
		return username

def get_new_username():
	"""prompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}!")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")	

