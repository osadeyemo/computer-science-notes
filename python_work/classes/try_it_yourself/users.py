class User:

	def __init__(self, first_name, last_name, age, username):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.username = username

	def describe_user(self):
		print(f"These are your information:")
		print(f"Firstname: {self.first_name}")
		print(f"Lastname: {self.last_name}")
		print(f"Age: {self.age}")
		print(f"Username: {self.username}")

	def greet_user(self):
		print(f"Hello {self.first_name} {self.last_name}.")

user_1 = User('azeez', 'salu', 35, 'azeezs')
user_2 = User('raissa', 'ndumu', 28, 'raissan')
user_3 = User('debo', 'adekoya', 33, 'deboa')

user_1.describe_user()
print('\n')
user_2.describe_user()
print('\n')
user_3.describe_user()
print('\n')
user_1.greet_user()
user_1.describe_user()
print('\n')
user_2.greet_user()
user_2.describe_user()
print('\n')
user_3.greet_user()
user_3.describe_user()
