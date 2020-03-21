pet_0 = {'type': 'cat', 'owner': 'azeez',}
pet_1 = {'type': 'dog', 'owner': 'moji',}
pet_2 = {'type': 'monkey', 'owner': 'wale',}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
	pet_type = pet['type'].title()
	pet_owner = pet['owner'].title()
	print(f"That {pet_type} is {pet_owner}'s pet.\n")