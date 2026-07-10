#Intro to lists
bicycles = ['trek', 'specialized', 'redline', 'connondale']
print(bicycles)

#Can access individual items in a list
print(bicycles[0].title())

#With Indexing 0 is the first position in a list
print(bicycles[1].lower())
print(bicycles[3].upper())
#Accessing the last
print(bicycles[-1].title())

#Combining indexing and f-strings
message = f'My favorite type of bicycle is: {bicycles[1].title()}'
print(message)

#Exercise 3.1
friends = ['chris', 'amanda', 'kyle', 'shelly', 'ted']
print(friends[0].title())
print(friends[-1].lower())
print(friends[-2].upper())
print(friends[1].title())
print(friends[2].title())

#Exercise 3.2
ted_message = f"Hello, {friends[-1].title()}, how is work today?"
print(ted_message)

amanda_message = f'{friends[1].upper()}, are you happy to be at work today?'
print(amanda_message)

shelly_message = f'Dear {friends[3].title()},\n\t how are you today?'
print(shelly_message)

#Exercise 3.3
transportation = ['tractor', 'car', 'bus', 'walking']
print(f'Yesterday I drove the {transportation[0]} all day.')
print(f'I drove to work today using a {transportation[1]}.')
print(f'This morning I took Rose {transportation[-1]}.')
print(f'Lastly, I would never consider taking the {transportation[2]} to work, ever.')

#Modifying lists
#Changing a list
motorcycles = ['honda', 'yamah', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#Appending (or adding) to the list
motorcycles = ['honda', 'yamah', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yahma')
motorcycles.append('suzuki')
print(motorcycles)

#Inserting into specific position
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'ducati') #Insert into first position
print(motorcycles)

#Removing elements
#Note, del deletes stuff permanently, can no longer access
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[-1]
print(motorcycles)

#Using pop to delete things
#Perserves what is deleted, starts from back by default (i.e., takes last in list)
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f'The last motorcycle I owed was {last_owned.title()}!')

#Can pop from any position
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}!")

#Removing items by values
#e.g., don't know position, only the value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#Working with the removed
#Only deletes the first occurance
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'{too_expensive.title()} was removed because it was too spendy!')

#Excercise 3.4
dinner_guests = ['amanda', 'kyle', 'shelly']
print(f'Dear {dinner_guests[0].lower()}, would you like to come to dinner with me?')
print(f'Dear, {dinner_guests[-1].upper()}, how does dinner sound?')
print(f'Would you come to dinner with me, {dinner_guests[1].title()}')

#Exercise 3.5
dinner_guests = ['amanda', 'kyle', 'shelly']
print(f'Unfortunately, {dinner_guests[0].title()} cannot make dinner.')
del dinner_guests[0]
print(dinner_guests)
dinner_guests.append('Rosie')
dinner_guests.insert(0, "Ted")
print(dinner_guests)

print(f'Pardon the inconvience, {dinner_guests[0]}, {dinner_guests[1].title()}, {dinner_guests[2].title()}, {dinner_guests[3]}, I have found us a larger table; thus more people will be coming!')

dinner_guests.insert(0,'Chris')
dinner_guests.insert(3,'Ryan')
dinner_guests.insert(-1,'barb')
print(dinner_guests)
dinner_guests.append('Kevin')
print(dinner_guests)

print(f"As it turns out, I can only invite two people to dinner...")

first_removed = dinner_guests.pop(-1)
print(f'Sorry, {first_removed.title()}, I fucking hate you. You cannot come to dinner')
second_removed = dinner_guests.pop(-2)
print(f'Likewise, {second_removed.title()}... Sorry not sorry.')
third_removed = dinner_guests.pop(3)
print(f"We can't all win, lo siento, {third_removed.title()}.")
print(dinner_guests)

#Remove everyone from the list
del dinner_guests[-1]
del dinner_guests[0]
del dinner_guests[0]
del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)

#Organizing a list
cars = ['bmw', 'audi', 'toyato', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyato', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyato', 'subaru']
print(f'\nHere is the original list:')
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars, reverse=True))
print(sorted(cars))

#Printing in reverse order
cars = ['bmw', 'audi', 'toyato', 'subaru']
print(cars)
cars.reverse()
print(cars)
cars.reverse()
print(cars)

#Finding the legnth of a list
cars = ['bmw', 'audi', 'toyato', 'subaru']
len(cars)

#Exercise 3.8
visit = ['japan', 'canada', 'mexico', 'china', 'germany']
print(f'\nHere is my list:')
print(visit)

print(f'\nHere is my list sorted:')
print(sorted(visit))

print(f"\nAs you can see, the sorted function does edit the original list:")
print(visit)

print(f"We can also go in reverse:")
print(sorted(visit, reverse=True))

print("Still not altered the orginal list:")
print(visit)

print("Now lets use the reverse method. Look at the results:")
visit.reverse()
print(visit)

print("\nNow let's turn it back:")
visit.reverse()
print(visit)

print("\nCan do the same thing with sort (permanent)")
visit.sort()
print(visit)

print("Lastly, let's sort in reverse order permanently:")
visit.sort(reverse=True)
print(visit)

#Exercise 3.9
print(len(dinner_guests))

#Exercise 3.10 (Using all function/methods we've learned)
