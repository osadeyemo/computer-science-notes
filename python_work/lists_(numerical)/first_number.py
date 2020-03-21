#to print numbers from 1 to 5, specify a range from 1 to 6
for value in range(1, 6):
	print(value)

for value in range(6):
	print(value)

#using range to create a list of numbers
numbers = list(range(1, 6))
print(numbers)

#how to list even numbers between 1 to 10
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#how to make the square of an integer frim 1 to 10
squares = []
for value in range(1, 11):
	square =  value ** 2
	squares.append(square)

print(squares)

squares = []
for value in range(1, 11):
	squares.append(value ** 2)

print(squares)

#how to find min, max, and sum of a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#or
digits = list(range(1, 11))
print(digits)

print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)


