name = "raissa"
print(name == "raissa")
print(name == "john")

print(name.lower() == "raissa")
print(name == "Raissa")

print(2 == 5)
print(4 != 6)
print(6 > 7)
print(6 < 7)
print(9 >= 2)
print(9 <= 2)

boyfriend = 'azeez'
girlfriend = 'raissa'
print(boyfriend == 'azeez' and girlfriend == 'raissa')
print(boyfriend == 'azeez' and girlfriend == 'joy')

print(boyfriend == 'azeez' or girlfriend == 'raissa')
print(boyfriend == 'azeez' or girlfriend == 'joy')

names = ['raissa', 'azeez', 'wale', 'moji', 'mike']
print(f"\n{'azeez' in names}")
print(f"\n{'mary' in names}")

print(f"\n{'taju' not in names}")

my_cars = ['benz', 'audi', 'lamborghini', 'ghost']
new_car = 'maybech'

if new_car not in my_cars:
	print(f"{new_car.title()} is not on the list.")
