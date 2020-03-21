friend_0 = {'first_name': 'morenike', 'last_name': 'salu', 'age': 33, 'city': 'upper marlboro'}
friend_1 = {'first_name': 'wale', 'last_name': 'adenola', 'age': 35, 'city': 'beltvile'}
friend_2 = {'first_name': 'raissa', 'last_name': 'ndumu', 'age': 28, 'city': 'woodbrigde'}

people = [friend_0, friend_1, friend_2]

for friend in people:
	name = f"{friend['first_name'].title()} {friend['last_name'].title()}"
	age = friend['age']
	city = friend['city'].title()
	print(f"\n{name}, of {city}, is {age} years old.")
