class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 3

	def describe_restaurant(self):
		print(f"{self.restaurant_name} sells {self.cuisine_type}.")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is open.")

	def set_number_served(self):
		print(f"{self.restaurant_name} has served {self.number_served} people today.")

	def increment_number_served(self, customers_per_day):
		self.number_served += customers_per_day

restaurant = Restaurant('Nagril', 'beef patties')
print(f"{restaurant.number_served}")
print('\n')

restaurant.number_served = 13
restaurant.set_number_served()
print('\n')

restaurant.increment_number_served(20)
restaurant.set_number_served()