favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

poll_lists = ['jen', 'sarah', 'phil', 'labi', 'ben']

for people in poll_lists:
	if people in favorite_languages.keys():
		print(f"\nHi {people.title()}, thank you for taking our poll.")
	else:
		print(f"\nHi {people.title()}, please take our poll.")