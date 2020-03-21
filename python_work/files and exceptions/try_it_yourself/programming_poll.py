filename = 'programming_poll.txt'

prompt = "Why do you like programming? "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	reason = input(prompt)

	if reason == 'quit':
		active = False

	else:
		with open(filename, 'a') as file_object:
			file_object.write(f"{reason}\n")