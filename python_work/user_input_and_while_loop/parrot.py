#user input
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

#
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

#use int() to accept numerical input
age = input("How old are you? ")
age = int(age)
age > 18

#
height = input("How tall you, inches? ")
height = int(height)

if height > 48:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

#the modulo operator
print(5 % 3)
print(4 % 2)
print(7 % 6)

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print(f"\nThe number is {number} is even.")
else:
	print(f"\nThe number {number} is odd.")

#while loops
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

#
prompt = "Tell us who you are, we can personalize the messages you see."
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
	message = input(prompt)

	if message != 'quit':
		print(message)

#using a flag
prompt = "Tell us who you are, we can personalize the messages you see."
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False

	else:
		print(message)

#using break to exit a loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	city = input(prompt)

	if city == "quit":
		break
	else:
		print(f"i'd love to go to {city.title()}!")

#using continue in a loop
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue

	print(current_number)

#avoiding infinite loop
x = 1
while x <= 5:
	print(x)
	x += 1

#using a while loop with lists and dictionaries
#moving items from one list to another


#start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#verify each user until there are no more unconfirmed users.
#move each verified user into the list of confirmed users.
while unconfirmed_users:
	current_users = unconfirmed_users.pop()

	print(f"Verifying user: {current_users.title()}")
	confirmed_users.append(current_users)

#display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

#removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'golfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)

#filling a dictionary with user input
responses = {}
#
#set a flag to indicate that polling is active.
polling_active = True

while polling_active:
	#prompt for the person's name and respnse.
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")

	#store the response in the dictionary.
	responses[name] = response
	
	#find out if anyone else is going to take the poll
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == 'no':
		polling_active = False

#polling is complete. show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
 	print(f"{name} would like to climb {response}.")