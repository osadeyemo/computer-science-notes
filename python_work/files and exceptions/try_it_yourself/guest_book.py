filename = 'guest_book.txt'

prompt = "Please enter your name: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	name = input(prompt)

	if name == 'quit':
		active = False

	else:
		print(f"\nHello, {name}!\n")

	with open(filename, 'a') as file_object:
		file_object.write(f"{name} was at the event.\n")