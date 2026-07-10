#Working with numbers
#Integers are whole numbers
print(3 + 2)
print(3-2)
print(3*2)
print(3/1)

#Order of operations
print(2+3*2)

#Floats: Anything with decimil 
print(.1+2.1)

#Divide integers and you get a float
print(4/2)
#Mix integer and float, you get a float
print(1.0 + 3)

#Generally use _ for long numbers instead of commas, more readable
#Python ignores the underscores
universe_age = 14_000_000_000
print(universe_age)

#Assigning multiple numbers to multiple variables at same time
x, y, z = 0, 1, 0
print(x, y, z)

#Use all caps when working with constants
MAX_CONNECTIONS = 5_000
print(MAX_CONNECTIONS)

#Exercise 2.9
print(3+1)
print(3/1)
print(5-1)
print(5*5)

favorite_number = 6

message = f"My favorite number is: {favorite_number}!"
print(message)