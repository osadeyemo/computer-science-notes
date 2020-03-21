prompt = "\nPlease add your pizza toppings: "
prompt += "\n(Please enter 'quit' when you are finished.) "

active = True
while active:
	pizza_toppings = input(prompt)

	if pizza_toppings == "quit":
		active = False
	else:
		print(f"\nAdding {pizza_toppings} to your pizza.")