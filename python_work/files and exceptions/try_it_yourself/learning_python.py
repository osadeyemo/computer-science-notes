
filename = 'learning_python.txt'


with open(filename) as file_object:
	lines = file_object.readlines()

my_lists = ''

for line in lines:
	my_lists += line

print(my_lists.replace('Python', 'Java'))

print(my_lists)