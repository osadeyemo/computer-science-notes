sandwich_orders = ['chickhen', 'turkey', 'ham', 'bacon', 'steak']
finished_sandwiches = []

while sandwich_orders:
	made_sandwich = sandwich_orders.pop()

	print(f"I made your {made_sandwich} sandwich.")
	finished_sandwiches.append(made_sandwich)

print("\nThis sandwiches have been made:")
for sandwich in finished_sandwiches:
	print(sandwich)