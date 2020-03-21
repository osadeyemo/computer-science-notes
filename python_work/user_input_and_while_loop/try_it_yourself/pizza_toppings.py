prompt = "\nPlease add your pizza toppings: "
prompt += "\n(Please enter 'quit' when you are finished.) "

while True:
	pizza_toppings = input(prompt)

	if pizza_toppings == "quit":
		break
	else:
		print(f"\nAdding {pizza_toppings} to your pizza.")