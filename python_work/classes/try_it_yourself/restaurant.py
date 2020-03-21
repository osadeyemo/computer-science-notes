class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"{self.restaurant_name} sells {self.cuisine_type}.")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is open.")

restaurant = Restaurant('Nagril', 'beef patties')

print(f"I ate launch at {restaurant.restaurant_name} today.")
print(f"I bought {restaurant.cuisine_type} for lunch today.")


restaurant.describe_restaurant()
restaurant.open_restaurant()