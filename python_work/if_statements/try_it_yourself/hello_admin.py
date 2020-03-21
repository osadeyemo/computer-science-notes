usernames =  ['azeezs', 'labis', 'owos', 'wales', 'admin']
for username in usernames:
	if username is 'admin':
		print(f"Hello {username}, would you like to see a status report?")
	else:
		print(f"Hello {username}, thank you for logging in again.")