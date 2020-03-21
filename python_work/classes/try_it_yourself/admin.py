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

class Admin(User):

	def __init__(self, first_name, last_name, age, username):
		super().__init__(first_name, last_name, age, username)
		self.privileges = ['can add post', 'can delete post', 'can ban user', 'can add new admin']

	def show_privileges(self):
		print(f"Hello {self.username}, these are your administrator's previleges:")
		for privilege in self.privileges:
			print(privilege)

site_admin = Admin('azeez', 'salu', 35, 'azeezs')
site_admin.show_privileges()
