current_users = ['azeez', 'raissa', 'wale', 'moji', 'john']

new_users =  ['bola', 'dapo', 'Raissa', 'AZEEZ', 'labi']

for new_user in new_users:
	if new_user.lower() in current_users:
		print(f"Sorry, {new_user} is already taken. Please enter a new username.")
	else:
		print(f"{new_user} is available.")

