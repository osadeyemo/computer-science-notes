#tuple = ()
#tuple cannot be change
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#tuple with one element
my_t = (3,)

#for loop
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#writing over a tuple
dimensions = (200, 50)
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 1000)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
