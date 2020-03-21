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

class Privileges:

	def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user', 'can add new admin']):
		self.privileges = privileges

	def show_privileges(self):
		print(f"These are your administrative previleges:")
		for privilege in self.privileges:
			print(privilege)

class Admin(User):

	def __init__(self, first_name, last_name, age, username):
		super().__init__(first_name, last_name, age, username)
		self.privileges = Privileges()

site_admin = Admin('azeez', 'salu', 35, 'azeezs')
site_admin.privileges.show_privileges()