def make_sandwich(*sanwiches):
	print("\nMaking the following sanwiches:")
	for sanwich in sanwiches:
		print(f"-{sanwich}")

make_sandwich('ham')
make_sandwich('chickhen', 'bacon')
make_sandwich('veggie', 'chickhen', 'turkey')
