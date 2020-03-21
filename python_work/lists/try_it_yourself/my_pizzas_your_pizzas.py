favorite_pizzas = ["cheese", "buffalo chickhen", "sausage"]
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append('veggei')
friend_pizzas.append('peperoni')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
	print(pizza.title())

print("\nMy friend's favorite pizza are:")
for pizza in friend_pizzas:
	print(pizza.title())