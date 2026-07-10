#Making variables
message = "Hello Python!"
print(message)

message = "Hello Python Crash Course!"
print(message)

#Exercise 2.1
greeting = "Good Morning, Thomas"
print(greeting)
greeting = "Goodnight, Thomas"
print(greeting)

#Different "types" of data
string = "Hello"

name = "thomas sease"
print(name.title()) #Uppercase
print(name.upper())
print(name.lower())


#Using F strings
first_name = "Thomas"
last_name = "sease"
full_name = f"{first_name} {last_name.title()}"
print(full_name)
print(f"Hello, {first_name.title()}, you are a coding genius!")

secret_message = f"{first_name.title()} {last_name.title()}, I am writing to tell you a secret message."
print(secret_message)

#Including White Space
print("Python")
#Add a indentation
print("\tPython")
#tabbing to a new line
message = f"My favorite languages are:\nSpanish\nJapanese\nEnglish"
print(message)

#Stripping extra white space in a character
#Can strip to the right, left, or everywhere
favorite_language = " python "
favorite_language = favorite_language.rstrip()
print(favorite_language)
favorite_language = favorite_language.lstrip()
print(favorite_language)
favorite_language = '  python. '
favorite_language = favorite_language.strip()
print(favorite_language)

#Stripping prefixes (e.g., website)
nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)

message = "One of Python's strengths is its diversity"
print(message)

