# Use the following string to practice the string methods below:

# "Everything is an Object in Python!!!"


# Convert the entire string to uppercase
# Convert the entire string to lowercase
# Convert only the first letter to uppercase

stringy = "Everything is an Object in Python!!!"
print(stringy)
print(stringy.upper())
print(stringy.lower())
print(stringy.capitalize())

first_name= "john"
last_name= "doe"
full_name= f"{first_name} {last_name}"

print(full_name)

print(f"Hello, {full_name.title()}")

phrase= " reindeer games "

print(phrase.rstrip())
print(phrase.lstrip())
print(phrase.strip())

Famous = "Valerie"

Quote = "Patience, young grasshopper"

print(f'{Famous} once said, "{Quote}."')
print("{} once said, '{}.'".format(Famous,Quote))

course= "Per Scholas"

print(course[1])
print(course[3])
print(course[-5])

string1= "Slicing strings is easy!"

print(string1[:3])
print(string1[1: 6: 2])
print(string1[-1: -8: -2])
print(string1[: : -1])

# Create a string to practice indexing and slicing on.

# Include at least one whitespace
# Include at least one special character
# Must have a length of at least 10
# Complete the following

# Reverse the entire string
# Get the last charachter of the string
# Get every other chrachter in the string
# Check the length of the string
# Get the 4th charachter in the string
# Get the 4th charachter through the 9th charachter in the string
# Get the 7th through last charachter in the string

reversed_string = "I am a stringy string."[::-1]

last_character = "I am a stringy string."[-1]

every_other_character = "I am a stringy string."[::2]

length_of_string = len("I am a stringy string.")

fourth_character = "I am a stringy string."[3]

slice_fourth_to_ninth = "I am a stringy string."[3:9]

slice_seventh_to_last = "I am a stringy string."[6:]





