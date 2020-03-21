class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"{self.restaurant_name} sells {self.cuisine_type}.")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is open.")

carabeian_restaurant = Restaurant('Nagril', 'beef patties')
nigerian_restaurant = Restaurant('Buka', 'jollof rice')
mexican_restaurant = Restaurant('Chipotle', 'burito')

carabeian_restaurant.describe_restaurant()
nigerian_restaurant.describe_restaurant()
mexican_restaurant.describe_restaurant()