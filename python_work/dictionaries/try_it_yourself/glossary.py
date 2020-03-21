glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

lis = "list"
dic = "dictionary"
loo = "loop"
stri = "string"
com = "comment"

print(f"{lis.title()}:\n\t {glossary['list']}")
print(f"{dic.title()}:\n\t {glossary['dictionary']}")
print(f"{loo.title()}:\n\t {glossary['loop']}")
print(f"{stri.title()}:\n\t {glossary['string']}")
print(f"{com.title()}:\n\t {glossary['comment']}")