#Working with Lists (Loops!)
#For loops

magicians = ['Gandolf', 'Byaz', 'Alice']
for magician in magicians:
    print(magician)

magicians = ['Gandolf', 'Byaz', 'Alice']
for magician in magicians:
    print(f'Hello, {magician.title()}, it is nice to meet you!')

magicians = ['Gandolf', 'Byaz', 'Alice']
for magician in magicians:
    print(f'{magician.title()} that was a good trick!')
    print(f"I can't wait to see your next trick, {magician.title()}!\n")

print("Thank you everyone. Those were great tricks!")

#Exercise 4.1
favorite_pizzas = ['sausage', 'cheese', 'pepperoni']
for pizza in favorite_pizzas:
    print(f'{pizza.title()} is a great flavor of pizza!')

favorite_pizzas = ['sausage', 'cheese', 'pepperoni']
for pizza in favorite_pizzas:
    print(f"\nI like {pizza.lower()} pizza!\n")

print("These are my favorite pizzas :)")

#Exercise 4.2-Animals
animals = ['Dog','Cat','Monkey']
for animal in animals:
    print(f'{animal.title()}')

for animal in animals:
    print(f"A {animal.lower()} would make a great pet!")

print("But I already have a pet!")

#Making numerical lists
#Range function

for value in range(1,5):
    print(value)

#Passing one argument, it knows to do 1-5
for value in range(6):
    print(value)

#Using range to make a list
numbers = list(range(6))
print(numbers)

#Can also skip numbers in a range
even_numbers = list(range(2,11,2))
print(even_numbers)
odd_numbers = list(range(1,10,2))
print(odd_numbers)

#Square numbers
#Creating empty list, getting numbers, multiplying them, putting them into squares variable on at a time
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

#Or more consicely
for value in range(1,11):
    squares.append(value**2)

print(squares)

#Simple statistics
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#List comprehensions (i.e., generating more complicated lists)
#Combines for loop and creation of new elements
squares = [value**2 for value in range(1,11)]
print(squares)

#Exercise 4.3
for number in range(1,21):
    print(number)

#Exercise 4.4
numbers = list(range(1,101))
for number in numbers: 
    print(number)

numbers = list(range(1,201))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1,21,2))
for odd_number in odd_numbers:
    print(odd_number)

threes = list(range(0,31,3))
for three in threes:
    print(three)

#4.8
cubes = []
for cube in range(1,11):
    cubes.append(cube**3)

for cube in cubes:
    print(cube)

cubes = [value **3 for value in range(1,11)]
print(cubes)

#Working with parts of a list
#"Slicing" through a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
#Stops one before three, so prints 0-2 (3 total names)
print(players[0:3])
print(players[1:4])

#If you omit first number, python starts at the beginning
print(players[:4])
#Also can take everything after certain number
print(players[2:])
#Can also do negatives
print(players[-3])
print(players[-3:])
#Can include a third value that will tell how many people to skip

#Looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(f"Here are the players:")
for player in players[:3]:
    print(player.title())

#Copying a list
my_foods = ['pizza', 'falefel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print(f"\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('yogurt')
friend_foods.append('oats')

print(my_foods)
print(friend_foods)

#Exercise 4.10 (Slices)
my_foods = ['yogurt', 'oats', 'protien bars', 'sandwiches', 'eggs', 'cheese']
print(f"The first three items in this list are:")
print(my_foods[:3])

print('Items from the middle are:')
print(my_foods[2:5])

print('The last three items are:')
print(my_foods[-3:])

#Exercise 4.11
my_pizzas = ['sausage', 'cheese', 'pepperoni', 'mushroom', 'bacon', 'veggie']
friends_pizzas = my_pizzas[:]

my_pizzas.append('bbq')
friends_pizzas.append('alfredo')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print(f"\nMy friend's favorite pizza's are:")
for pizza in friends_pizzas:
    print(pizza)

#4.12
my_foods = ['yogurt', 'protein bar', 'apples', 'pineapple']

print("These are my favorite foods:")
for food in my_foods:
    print(food)

#This one is cool... Sorted and used a slice
print('These are my top 3 foods:')
for food in sorted(my_foods[0:3]):
    print(food.title())

#Tuples
#Essentially lists that cannot change
dimensions = (200, 50)

#Can still index
print(dimensions[0])
print(dimensions[1])

#Can also loop through tuples
for dimension in dimensions:
    print(dimension)

#Writing over a truple
dimensions = (200, 50)
print("Original Diminensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print(f"\nModified Diminesions:")
for dimension in dimensions:
    print(dimension)

#Excercise 4.13 Buffet
buffet_foods = ('meat', 'ice cream', 'cake', 'potatoes', 'pasta')
print("The foods at my favorite buffet are:")
for food in buffet_foods:
    print(food.title())

buffet_foods = ('stew', 'clam chowder', 'cake', 'potatoes', 'pasta')
print("Here is the revised menu:")
for food in buffet_foods:
    print(food)

