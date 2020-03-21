prompt = "\nPlease enter your age: "
prompt += "\nEnter 'quit' when you are finished. "

while True:
	age = input(prompt)
	if age == 'quit':
		break
	age = int(age)
	if age < 3:
		print("Your ticket price is free.")
	elif age <= 12:
		print("Your ticket price is $10 please.")
	else:
		print("Your ticket price is $15 please.")