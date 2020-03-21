cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#condition tests
car = "bmw"
print(car == 'bmw')

car = "audi"
print(car == 'bmw')

#case 
car = "Audi"
print(car == 'audi')
print(car.lower() == 'audi')
print(car)

#checking for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#numerical comparisons
age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("This is not the correct answer. Please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

#using 'and' to check multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

#using 'or' to check multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

#checking whether a value is in a list = 'in'
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

#checking whether a value is not in a list = 'not'
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

#boolean expressions = True or Flase

#if statements 
age = 19
if age >= 18:
    print("You are old engouh to vote!")
    print("Have you registered to vote yet?")

#if-else statements
age = 17
if age >= 18:
    print("You are old engouh to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote!")
    print("Please register to vote as soon as you turn 18!")

#if-elif-else chain
age = 12

if age < 4:
    print("Your admission cost is $).")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost $40.")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

#multiple elif blocks 
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")

#testing multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']

if "mushrooms" in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza.")

#if statements and list
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f'Adding {requested_topping}.')

print('\nFinished making your pizza!')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print('\nFinished making your pizza!')

#checking that a list is not empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#using multiple lits
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french_fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")