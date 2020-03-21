print("Give me two numbers, and I will add them.")

first_number = input("\nFirst number: ")
second_number = input("Second number: ")
try:
	answer = int(first_number) + int(second_number)
except ValueError:
	print("Value must be numerical not alphabetical.")
else:
	print(answer)