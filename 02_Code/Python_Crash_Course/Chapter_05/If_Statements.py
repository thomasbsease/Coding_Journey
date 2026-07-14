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
car = 'suburu'
print("Does car == 'suburu? I predict true!")
print(car == 'suburu')

age = 18
print("Is age greater than 20?")
if age < 20:
    print("Sorry, you are not old enough!")

age_1 = 20
age_2 = 30

print("Are both ages larger than 25?")
print(age_1 > 25 and age_2 > 25)
print("how about either or?")
print(age_1 > 25 or age_2 > 25)

car = 'Toyota'
print(car.lower() == 'toyota')

ingredients = ['flour', 'cheese', 'pepperoni', 'baking soda']
print('flour' in ingredients)

if 'mushrooms' not in ingredients:
    print('Hold the mushrooms!')

#If statements
age = 19
if age >= 18: 
    print("You are old enough to vote!")
    print("Do you need help registering?") #Can have multiple commands after if statement

#If-Else statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print('Do you need help registering?')
else: 
    print("You are not old enough to vote.")
    print("Come back when you are 18!")

#If-elif-else statement (i.e., testing more than 2 conditions)
age = 11
if age < 4:
    print("You get in free!")
elif age < 12:
    print("You must pay 5 dollars!")
else:
    print("You must pay 10 dollars!")

#More concisely
age = 12
if age < 4:
    price = 0
if age < 18:
    price = 25
else: 
    price = 40

print(f"Your price of admission is ${price}")

#Using multiple elif blocks
#Can use as many as you like
age = 70

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your price of admission is ${price}")

#Don't need the else block
age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your price of admission is ${price}")

#Testing multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print('\nFinished making your pizza!')

#Exercise 5.3 (Alien Colors)
alien_color = "red"
if alien_color == 'red':
    print("You win 5 points!")
if alien_color == 'green':
    print("You win ten points!")

#Exercise 5.4
alien_color = 'red'
if alien_color == 'red':
    print("You win 10 points")
else:
    print('You get 15 points!')

alien_color = 'green'
if alien_color == 'red':
    print("You win 10 points")
else:
    print('You get 15 points!')

#Exercise 5.5
alien_color = 'yellow'
if alien_color == 'red':
    print("You win 5 points")
elif alien_color == 'green':
    print("You win 10 points!")
elif alien_color == 'yellow':
    print("You win 15 points!")

#Exercise 5.6
age = 70
if age < 2:
    print("You are a baby")
elif age >= 2 and age < 4:
    print('You are a toddler')
elif age >= 4 and age < 13:
    print("You are a kid!")
elif age >= 13 and age < 20:
    print("You are a teenager!")
elif age >= 20 and age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are an elder")

#Exercise 5.7
favorite_fruit = ['pineapple', 'apple', 'blueberry']
if 'pineapple' in favorite_fruit:
    print("You really like pineapple!")
if 'blackberry' in favorite_fruit:
    print("You really like blackberries!")
if 'apple' in favorite_fruit: 
    print("You really like apples!")
if 'blueberry' in favorite_fruit:
    print("You really like blueberries")
if 'mango' in favorite_fruit:
    print("You really like mangos!")
print('\nThose are your favorite fruits!')

#Using an if statement with a list
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in requested_toppings:
    print(f"Adding {topping}")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in requested_toppings:
    if topping == 'green peppers':
        print(f"Sorry, we are out of {topping}")
    else:
        print(f"Adding {topping} to your pizza")

print("\nFinished making your pizza!")

#Checking to see if list is empty
my_toppings = []

if my_toppings:
    for topping in my_toppings:
        print(f"Adding {topping} to your pizza!")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#Using multiple lists
available_toppings = ["mushrooms", 'olives', 'green peppers', 
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping} to your pizza")
    else:
        print(f"Sorry, we don't have {requested_topping}")

print("Finished making your pizza!")

#Exercise 5.8
usernames = ['amanda123', 'tomcat', 'kylekyle', 'shellsbells', 'tedward', 'admin']

for user in usernames:
    if user == 'admin':
        print(f"Hello, {user}, would you like see a summary report?")
    else:
        print(f"Hello, {user}, its good to see you again!")

#Exercise 5.9
usernames = ['amanda123', 'tomcat', 'kylekyle', 'shellsbells', 'tedward', 'admin']

if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"\nHello, {user}")
        else:
            print(f"\nHello, {user}. It's good to see you again")

#Exercise 5.10
current_users = ['amanda123', 'Tomcat', 'kylekyle', 'shellsbells', 'tedward']

for user in current_users:
    existing_users = user.lower()

new_users = ['ryan', 'barb', 'indie', 'amanda123', 'TOMCAT']

for user in new_users:
    if user.lower() in existing_users:
        print(f"Sorry, {user} is not an availble username")
    else:
        print(f"Great news! {user} is an available username!")

numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2 or number == 3:
        print(f"{number}nd")
    else:
        print(f"{number}th")

    
