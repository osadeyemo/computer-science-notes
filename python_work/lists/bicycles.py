#list = [] and individual item in the list are separated by commas ","
#index start at 0, not 1
#the first item in a list is at position 0

bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)

#accessing the item in a list with index
print(bicycles[0])
print(bicycles[1])
print(bicycles[3])

#accessing the item in a list and changing the case
print(bicycles[0].title())

#accessing the last syntax in a list = [-1]
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#modifying item in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#change the fist element in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

#adding item to a list = .append()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

#appending item to an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#inserting item into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#removing item from a list using del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#removing item from a list using pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

#removing any item from any position in a list using pop
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#removing an item from a list by value. = .romove()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

#organizing and sorting a list in alphabetical order = .sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#sorting a list in reverse alphabetical order = .sort(reverse=True)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#sorting a list temporarily = sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#sorting a list temporarily in reverse = sorted()
print("\nHere is the sorted list:")
print(sorted(cars, reverse=True))

#print a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

#finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

#for loop
magicians = ['john', 'ali', 'alex', 'mike']
for magician in magicians:
	print(magician)

magicians = ['john', 'ali', 'alex', 'mike']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick.")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show.")

#slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

#looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team")
for player in players[0:3]:
	print(player.title())

#copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy frined's favoritefoods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy frined's favoritefoods are:")
print(friend_foods)