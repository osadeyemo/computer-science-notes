alien_color = 'green'

if alien_color is 'green':
	print(f'You just earned 5 points for shooting {alien_color} alien.')

alien_color = 'yellow'

if alien_color is not 'green':
	print("You just earned 10 points.")

alien_color = 'yellow'

if alien_color is 'green':
	print(f'You just earned 5 points for shooting {alien_color} alien.')
else:
	print("You just earned 10 points.")