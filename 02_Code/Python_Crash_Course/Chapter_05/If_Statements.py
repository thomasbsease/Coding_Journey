#Chapter 5 (If statements)
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Equality operator "=="
car = 'bmw'
print(car == 'bmw')

car = 'toyota'
print(car == 'bmw')

#Is case sensitive
car = "Audi"
print(car == 'audi')
print(car.lower() == 'audi')

#Inequality operator "!="
requested_toppings = 'mushrooms'

if requested_toppings != "anchovies":
    print('Hold the anchovies!')

#Numeric comparisons
age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("That is not the right answer! Try again")

#Can also do other comparisons
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

#Checking multiple conditions using AND
age_0 = 22
age_1 = 18

print(age_0 >= 21 and age_1 >= 21)

age_3 = 22
age_4 = 22

print(age_3 >= 20 and age_4 >= 20)

#Can also do OR
age_0 = 22
age_1 = 18

print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

#Checking whether a value is in a list
# IN
requested_toppings = ['cheese', 'mushrooms', 'onions']

print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

#Whether value is not in a list
# NOT IN
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, welcome to our community. You can post a response!")

#Boolians (True or False)
game_active = True
can_edit = False

#Exercise 5.1

