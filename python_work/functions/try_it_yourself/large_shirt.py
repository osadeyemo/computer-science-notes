def make_shirt(shirt_size= 'large', shirt_message= 'i love python'):
	print(f"You ordered a {shirt_size} shirt that says: '{shirt_message.title()}'.")

make_shirt()
make_shirt(shirt_size= 'medium')
make_shirt('small', 'i love cokkies')
make_shirt(shirt_message= 'i love you', shirt_size= 'extra small')