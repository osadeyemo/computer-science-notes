favorite_numbers = {
	'jen': [6, 2, 1],
	'sarah': [9, 3, 4],
	'edward': [10, 6, 10],
	'phil': [7, 23, 12],
	'mary': [3, 90,],
	}

print(f"Jen's favorite numeber is {favorite_numbers['jen']}.")
print(f"Sarah's favorite numeber is {favorite_numbers['sarah']}.")
print(f"Edward's favorite numeber is {favorite_numbers['edward']}.")
print(f"Phil's favorite numeber is {favorite_numbers['phil']}.")
print(f"Mary's favorite numeber is {favorite_numbers['mary']}.")
print("\n")
#or 
for name, numbers in favorite_numbers.items():
	name = name.title()
	print(f"{name} favorite numbers are:")
	for number in numbers:
		print(f"{number}")