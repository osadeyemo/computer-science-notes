sandwich_orders = ['chickhen', 'pastrami', 'turkey', 'ham', 'pastrami', 'bacon', 'pastrami', 'steak']
finished_sandwiches = []
print(f"We are out of pastrami.\n")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	made_sandwich = sandwich_orders.pop()

	print(f"I made your {made_sandwich} sandwich.")
	finished_sandwiches.append(made_sandwich)

print("\nThis sandwiches have been made:")
for sandwich in finished_sandwiches:
	print(sandwich)