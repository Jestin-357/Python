 # variables
x = 5
x = "hello there"
print(x)

# casting
# If you want to specify the data type of a variable, this can be done with casting.

x = str(4)
y = int(5)
z = float(6)

print(x,y,z)

# Many Values to Multiple Variables
x,y,z = "orange", 'banana', "cherry"
print(x)
print(x,y,z)

# One Value to Multiple Variables
x = y = z = "orange"
print(x,y,z)

# Unpack a Collection
fruits = ['apple','banana,'cherry']

# Local Variables
x = 'awesome'
def myfun():
    print('python is ' + x)
myfun()

# Create a variable inside a function, with the same name as the global variable
x = 'fantastic'

def myfun():
    x = ' awesome'
    print('python is ' + x)
myfun()
 # here not able to use the local varible outside the function
print(x)

# Global Variables
#Normally, when you create a variable inside a function, that variable is local, and can only be used inside 
#that function.
#to create a global variable inside a function, you can use the global keyword.

def myfun():
    global x
    x = 'Fantastic'
    print('python is ' + x)
myfun()
 # here we can take out the global variable and use it outside the function
print(x)


print(type(x))


# Python Data Types
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType


to know  data type of any object by using the type() function:

x = 5
print(type(x))

x = range(4)
print(x)

# In Python, the data type is set when you assign a 
# value to a variable:


x = 'hello world'
print(type(x))

x = 20 
print(type(x))

x = 1j 
print(type(x))

x = ['apple','banana','orange']
print(type(x))


x = ('apple','banana','orange')
print(type(x))

x = {'name': 'jestin'}
print(type(x))

x = {"apple", "banana", "cherry"}
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(type(x))

x = True
print(type(x))


# python numbers

There are three numeric types in Python:
int
float
complex

com = 2j
type(com)

Type Conversion
# we can convert from one type to another with the int(), float(), and 
# complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert from int to float
a = float(x)
a

# convert float to int
b = int(y)
b

c = complex(x)
c
#Note: You cannot convert complex numbers into another number type.

Random Number
# python does not have a random() function to make the random number

import random
# display a random number from 1 to 30:
print(random.randrange(1,30))

# strings
Strings in python are surrounded by either single quotation marks, 
or double quotation marks.

'hello' is the same as "hello".

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

## multiline strings
### You can assign a multiline string to a variable by using three quotes(""" """):

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

a = "Hello"
print(a[2])

Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.


for x in "banana":
    print(x)


String length
To get the length of a string, use the len() function.

a = "Hello World"
print(len(a))

Check string 
To check if a certain phrase or character is present in a string, we can use the keyword in.


txt = "The best things in life are free!"
print("free" in txt)

#. Using if statement
if "free" in txt:
    print(" it is present")
else:
    print("not present")


# check if not 
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("it is not present")
else:
    print(" present")









