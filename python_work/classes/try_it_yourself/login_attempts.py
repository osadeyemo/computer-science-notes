class User:

	def __init__(self, first_name, last_name, age, username):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.username = username
		self.login_attempts = 0

	def describe_user(self):
		print(f"These are your information:")
		print(f"Firstname: {self.first_name}")
		print(f"Lastname: {self.last_name}")
		print(f"Age: {self.age}")
		print(f"Username: {self.username}")

	def greet_user(self):
		print(f"Hello {self.first_name} {self.last_name}.")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

user_1 = User('azeez', 'salu', 35, 'azeezs')
user_1.describe_user()
user_1.greet_user()


print('\nMaking 3 login attempts....')
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"	Login attempts: {user_1.login_attempts}")

print("Resetting login attempts...")
user_1.reset_login_attempts()
print(f"	Login attempts: {user_1.login_attempts}")
