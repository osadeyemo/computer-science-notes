#springs 
"This is a string."
'This is also a string.'
'I told my friend, "Python is my favorite languange!"'
"The languange 'Python' is named after Monty Python, not the snake."
"One of Python's strength is its divirse and supportive community."

#changing case in a string with method = .title(), .upper(), .lower()
name = "ada lovelace"
print(name.title())

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())


#Using variables in strings = f-strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name.title())
print("Hello, " + full_name.title())

#adding whitespace to strings with tabs or newlines

#tab = \t
print("\tPython")

#newline = \n
print("Languages:\nPython\nC\nJavaScript")

#newline and tab = \n\t
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#stripping whitespace from value = .rstrip(), .lstrip(), .strip()
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())

#stripping whitespace from variable pamanently = .rstrip()
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

#stripping whitespace = .rstrip(), .lstrip(), .strip()
favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
