#Chapter 6 (Dictionaries)
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#Simple dictionary and access value based on key
alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You recieve {new_points} points!")

#Adding to existing dictionary 
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print(len(alien_0))

#Starting with empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#Modifying a dictionary
alien_0 = {'color': "green", 'points': 5}
print(f"This is the alien's color: {alien_0['color']}")
alien_0['color'] = 'red'
print(f"Here is the alien's new color: {alien_0['color']}")

#Another example
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Original position: {alien_0['x_position']}")

#Move alien to the right
#Determine how far based on speed
if alien_0['speed'] == 'slow':
    x_increment = 1 
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"This is the new position of the alien: {alien_0['x_position']}")

#Removing key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

#Removes permanently 
del alien_0['points']
print(alien_0)

#Dictionary of similar objects
favorite_languages = {
    'jen': 'python',
    'sara': 'c', 
    'edward': 'rust', 
    'phil': 'python',
    }
language = favorite_languages['jen'].title()
print(f"Jen's favorite langugage is {language}!")
print(favorite_languages['sara'])

#Using get() to access values
alien_0 = {'color': 'green', 'speed': 'slow'}
#alien_0['points']-- results in error

#Similar to accessing value, but returns section arugment if it doesn't exist
point_value = alien_0.get('points', 'No Point Value Assigned')
print(point_value)

#Exercise 6.1
amanda = {'hair': 'brown', 'height': 72, 'eyes': 'brown', 'pregnant': 'yes'}
print(amanda['hair'])
print(amanda['eyes'])
print(amanda['pregnant'])
print(amanda['height'])

#Exercise 6.2 (favorite numbers)
favorite_numbers = {
    'tom': 6,
    'amanda': 3,
    'kyle': 7,
    'shelly': 1,
    'ted': 0,
    }

print(f"Tom's favorite number is {favorite_numbers['tom']}!")
print(f"Shells favorite number is {favorite_numbers['shelly']}!")

#Exercise 6.3
programing_words = {
    'if_else': "a statement that makes a comparison", 
    'dictionary': 'a storage unit for multiple types of information',
    'list': 'storage unit for one type of information'
    }

print(f"\nA dictionary is a:\n\t{programing_words['dictionary']}.")
print(f"\nAlternatively, a list is a:\n\t{programing_words['list']}")

#Looping through a dictionary
#Can go through values, the keys, or values and keys
user_0 = {
    'username': 'thomasbsease',
    'first': 'thomas',
    'last': 'sease',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

#Another example
favorite_languages = {
    'jen': 'python',
    'sara': 'c', 
    'edward': 'rust', 
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite langugage is {language}!")

#Loop through all keys in dictionary-- keys()
favorite_languages = {
    'jen': 'python',
    'sara': 'c', 
    'edward': 'rust', 
    'phil': 'python',
    }

for name in favorite_languages.keys():
    print(f"{name.title()}")

#More complicated example
favorite_languages = {
    'jen': 'python',
    'sara': 'c', 
    'edward': 'rust', 
    'phil': 'python',
    }

friends = ['jen', 'edward']
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

#Checking if someone took the poll
favorite_languages = {
    'jen': 'python',
    'sara': 'c', 
    'edward': 'rust', 
    'phil': 'python',
    }

if 'Erin' not in favorite_languages.keys():
    print("Erin, please take the poll!")

#Looping through dictionary in a particular order
favorite_languages = {
    'jen': 'python',
    'sara': 'c', 
    'edward': 'rust', 
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys(), reverse=True):
    print(f"\t{name.title()}, thank you for taking the poll!")

#Looping through all values--values()
favorite_languages = {
    'jen': 'python',
    'sara': 'c', 
    'edward': 'rust', 
    'phil': 'python',
    }

print("Here were the languagues chosen by our particpants:")
for language in favorite_languages.values():
    print(language.title())

#If there are repeats (people same answer) use set()
print("\nHere is everyone's favorite languages:")
for language in set(favorite_languages.values()):
    print(f"\t{language.title()}")