import math

# String data type

# Literal assignment of values
first = "Dave"
last = "Gray"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Constructor
pizza = str("pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last

fullname += '!'
print(fullname)

# casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?                                               

I was just checking in.       

                    All good?
'''
print(multiline)

# escaping special characters
sentence = 'I\m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "okay"))
print(multiline)

print(len(multiline))
multiline += "                                 "
multiline = "                     " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(20, ".") + "$1".rjust(4))
print("Muffin".ljust(20, ".") + "$2".rjust(4))
print("Cheesecake".ljust(20, ".") + "$4".rjust(4))

print("")

# string index values
print(first[1]) # indexes start at 0 # a
print(first[-1]) # r
print(first[1:-1]) # arke
print(first[1:]) # arker

# some methods return boolean data
print(first.startswith("P")) # True
print(first.endswith("r")) # True

# boolean data type
myvalue =  True # must have capitalized first letter
myvalue = False # must have capitalized first letter

x = bool(False)
print(type(x))
print(isinstance(x, bool))

# Numeric data types

# integer
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float (decimal)
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built-in math functions

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# error if you attempt to cast incorrect data
# zip_value = int("New York")
