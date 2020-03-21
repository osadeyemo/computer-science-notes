nigerian_languages = ['yoruba', 'igbo', 'hausa']

#accessing the item in a list with index
print(nigerian_languages[0].title())

#accessing the last item in a list = [-1]
print(f"\n{nigerian_languages[-1].title()}")

#change the first item in a list
nigerian_languages[2] = 'edo'
print(f"\n{nigerian_languages}")

#adding item to a list = .append()
nigerian_languages.append('calabar')
print(f"\n{nigerian_languages}")

#inserting item into a list
nigerian_languages.insert(2, 'hausa')
print(f"\n{nigerian_languages}")

#removing item from a list using del statement
del nigerian_languages[4]
print(f"\n{nigerian_languages}")

#removing item from a list using pop() method
nigerian_languages.pop()
print(f"\n{nigerian_languages}")

#removing an item from a list by value. = .remove()
nigerian_languages.remove('igbo')
print(f"\n{nigerian_languages}")

#organizing and sorting a list in alphabetical order = .sort()
nigerian_languages.sort()
print(f"\n{nigerian_languages}")

#sorting a list in reverse alphabetical order = .sort(reverse=True)
nigerian_languages.sort(reverse=True)
print(f"\n{nigerian_languages}")

#sorting a list temporarily = sorted()
print(f"\n{sorted(nigerian_languages)}")

#sorting a list temporarily in reverse = sorted()
print(f"\n{sorted(nigerian_languages, reverse=True)}")

#print a list in reverse order
nigerian_languages.reverse()
print(f"\n{nigerian_languages}")

#finding the length of a list
print(f"\n{len(nigerian_languages)}")










