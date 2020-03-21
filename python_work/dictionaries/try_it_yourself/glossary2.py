glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'if-elif-else': "Are used for conditional branching or decision making.",
    'import': 'Is used to import modules into the current namespace.',
    'lambda': 'Is used to create an anonymous function (function with no name).',
    'finally': 'Is used with try…except block to close up resources or file streams.',
    'class': 'Is used to define a new user-defined class in Python.',
    }

for key, value in glossary.items():
	print(f"\n{key.title()}: {value}")