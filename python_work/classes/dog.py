#creating a Dog class
class Dog:
	"""A simple attempt to model a dog."""

	def __init__(self, name, age): #this is a method
		"""Initialize name and age attributes."""
		self.name  = name
		self.age = age 

	def sit(self): #this is a method
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self): #this is a method
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")

#Making an instance fron a class
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#calling methods
class Dog:
	"""A simple attempt to model a dog."""

	def __init__(self, name, age): 
		"""Initialize name and age attributes."""
		self.name  = name
		self.age = age 

	def sit(self): 
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

#creating multiple instances 
class Dog:
	"""A simple attempt to model a dog."""

	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name  = name
		self.age = age 

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6) #this is an instance
your_dog = Dog('Lucy', 3) #this is an instance

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")

#working with classes and instances 

class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

#setting a default value for an attribute
class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Printa statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#modifying attribute's value directly
class Car:
	"""A simple attempt to represent a car."""
	
	def __init__(self, make, model, year):
		"""initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Printa statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#modifying an attribute's value through a method
class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Printa statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""set the odometer reading to the given value.
           reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage

		else:
			print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

#incrementing an attribute's value through a method
class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Printa statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""set the odometer reading to the given value.
           reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage

		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""add the given amount to the odometer reading"""
		self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', '2015')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#inheritance
class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Printa statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""set the odometer reading to the given value.
           reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage

		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""add the given amount to the odometer reading"""
		self.odometer_reading += miles

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class."""
		super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

#Defining attributes and methods for the child class
class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Printa statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""set the odometer reading to the given value.
           reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage

		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""add the given amount to the odometer reading"""
		self.odometer_reading += miles

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery_size = 75

	def describe_battery(self):
		"""Print statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kwh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

#Overriding methods from the parent class by naming the child class the same name as the parent method = page 170

#intances as attributes
class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Printa statement showing the car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""set the odometer reading to the given value.
           reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage

		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""add the given amount to the odometer reading"""
		self.odometer_reading += miles

class Battery:
	"""A simple attempt to model a bettery for an electric car."""

	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kwh battery.") 

	#adding another method to battery
	def get_range(self):
		"""print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge.")
		
class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#Importing classes = page 174

#importing a single class = page 

#storing multiple classes in a module = page 175

#importing multiple classes from a module = page 177

#importing an entire module = page 177

#Importing all classes from module = page 177

#importing a module into a module

#aliases = page 179

#python standard library = page 180

from random import randint
print(randint(1,6))

from random import choice 
players = ['charles', 'martina', 'michael', 'florence', 'eli']
frist_up = choice(players)
print(frist_up)