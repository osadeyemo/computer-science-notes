class Die:

	def __init__(self, sides= 6):
		self.sides = sides

	def roll_die(self):
		from random import randint
		print(randint(1,self.sides))

six_sided_die = Die()

for num in range(10):
	num = six_sided_die.roll_die()
print(num)

d10 = Die(sides= 10)

for num in range(10):
	num = d10.roll_die()
print(num)

d20 = Die(sides= 20)

for num in range(10):
	num = d20.roll_die()
print(num)