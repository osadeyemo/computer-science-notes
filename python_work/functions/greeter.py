#defining a function
def greet_user ():
	"""Display a simple greeting."""
	print("Hello!")

greet_user()

#passing information to a function
def greet_user(username):
	"""Display a simple greeting."""
	print(f"Hello, {username.title()}!")

greet_user('jesse')

#positional aruguments
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie') #multiple functin calls

#keyword aguments
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type= 'hamster', pet_name= 'harry')
describe_pet(pet_name= 'harry', animal_type= 'hamster')

#default values
def describe_pet(pet_name, animal_type= 'dog'):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name = 'willie')

#equivalent function calls
#
#A dog name Willie.
describe_pet('willie')
describe_pet(pet_name= 'willie')

#A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name= 'harry', animal_type= 'hamster')
describe_pet(animal_type= 'hamster', pet_name= 'harry')

#returning a simple value
def get_formatted_name(first_name, last_name):
	"""Return a full name neatly formatted"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#making an argument optional
def get_formatted_name(first_name, last_name, middle_name= ''):
	"""Return a full name neatly formatted"""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#retruning a dictionary
def build_person(first_name, last_name):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age= None):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', age= 27)
print(musician)

#using a function with a while loop
def get_formatted_name(first_name, last_name):
	"""Return a full name neatly formatted"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

#This is an infinite loop!
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")

	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}!")

#passing a list
def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
		msg = f"Hello, {name.title()}!"
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#modifying a list in a function

#Start with some designs that need to be printed.
unprinted_designs = ['phone_case', 'robot pendant', 'dodecahedron']
completed_models = []

#simulate printing each design, until none are left.
#move each design to completed_models after printing.
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Printing model: {current_design}")
	completed_models.append(current_design)

#Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)

#with a function
def print_models(unprinted_designs, completed_models):
	#simulate printing each design, until none are left.
	#move each design to completed_models after printing.
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	#Display all completed models.
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['phone_case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

#to prevent a function from modifying a list, make a copy of the list.

#passing an arbitrary number of arguments 
def make_pizza(*toppings):
	"""Print the list of toppings that have been requested."""
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

#Summarize the pizza we are about to make.
def make_pizza(*toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

#mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

#using arbitrary keyword arguments
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein', location= 'princeton', field= 'physics')
print(user_profile)

#storing your functions in modules 

#importing an entire module = page 151
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

#importing specific functions = page 152
from pizza import make_pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

#using as to give a function a alias = page 152
from pizza import make_pizza as mp

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

#using as to give a module an alias = page 153
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

#importing all functions in a module = page 153
from pizza import *

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
