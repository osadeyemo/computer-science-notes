players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("The first three items in the list are:")
for player in players[0:3]:
	print(player.title())

print("\nThree items from the middle of the list are:")
for player in players[1:4]:
	print(player.title())

print("\nThe last three items in the list are:")
for player in players[-3:]:
	print(player.title())