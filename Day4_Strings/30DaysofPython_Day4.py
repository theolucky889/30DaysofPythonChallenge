# Create a string
letter = 'p'                # A string could be a single character or a bunch of texts\
print(letter)               # p
print(len(letter))          # 1
greeting = 'Hello World!'   # String could be made using a single or double quote, "Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

# Multiline string is created by using single(''') or triple double quotes("""")
multiline_string = '''I am a student and enjoy learning.
I didn't find anything as rewarding as learning new things.
That is why I am learning python again.'''
print(multiline_string)

# Another way of doing the same thing is by using (""")

# String Concatenation
# We can connect strings together. Merging or connecting strings is called concatenation.
first_name = "Theodore Lucky"
last_name = "Tendy"
space = " "
full_name = first_name + space + last_name
print(full_name)    # Theodore Lucky Tendy
# Checking the length of a string using len() built-in function
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

# Escape sequence in strings
# In python and other programming languages \ followed by a character is an escape sequence
"""
- \n : new line
- \t : Tab means (8 spaces)
- // : back slash
- \' : single quote (')
- \" : double quote (")    
    """
# Let's see the use of the above escape sequences with examples
print("I hope I will be better at python. \nAm I ?")    # line break
print("Days\tTopics\tExercises")    # adding tab spaces or 4 spaces
print("Day 1\t5\t5")
print("Day 2\t6\t20")
print("Day 3\t5\t23")
print("Day 4\t1\t35")
print("This is a blackslash symbol (\\)")   # To write backslash
print("In every programming language it starts with \"Hello, World!\"") # To write a double quote inside

# String Formatting
#   Old style string formatting (% Operator)
"""
In python, there are many ways of formatting strings. The "%"
operator is used to format a set of variables enclosed in a "tuple"
(a fixed list), together with a format string, which containts
normal text together with "argument specifiers", special symbols
like "%s", "%d", "%f", "%.number of digitsf".
- %s = String (or any object with string representation, like numbers)
- %d = integers
- %f = floating point numbers
- "%.number of digitsf" = Floating point numbers with fixed precision
    """

# Strings only
first_name = "Theodore Lucky"
last_name = "Tendy"
language = "Python"
formated_string = "I am %s %s. I am learning %s" %(first_name, last_name, language)
print(formated_string)

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = "The area of circle with a radius %d is %.2f" %(radius, area)     # 2 refers the 2 significant digits after the decimal point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = "The following are python libraries:%s" %(python_libraries)
print(formated_string)

# NEW style string formatting (str.format)
# Introduced in Python3

first_name = "Theodore Lucky"
last_name = "Tendy"
language = "Python"
formated_string = "I am {} {}. I am learning {}".format(first_name, last_name, language)
print(formated_string)

a = 4
b = 3

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = "The area of a circle with a radius {} is {:.2f}.".format(radius, area)
print(formated_string)

# String Interpolation / f-Strings (Python 3.6+)
c = 4
d = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# Python Strings as Sequences of Characters
"""
Python strings are sequences of characters, and share their basic methods of access with other
python ordered sequences of objects, lists and tuples. THe simplest way of extracting single
characters from strings (and individual members from any sequence) is to unpack them into
corresponding variables
    """
# Unpacking Characters
language = "Python"
a,b,c,d,e,f = language      # Unpacking sequence characters into variables
print(a)    # P
print(b)    # y
print(c)    # t
print(d)    # h
print(e)    # o
print(f)    # n

# Accessing Characters in Strings by index
"""
In programming, counting starts from zero. Therefore the first letter of a string is at zero
index and the last letter of a string is the length of a string minus one.
    """
language = "Python"
first_letter = language[0]
print(first_letter)     # p
second_letter = language[1]
print(second_letter)    # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)      # n

# If we want to start from right end, we can use negative indexing, -1 is the last index
language = "Python"
last_letter = language[-1]
print(last_letter)  # n
second_last = language[-2]
print(second_last)  # o

# Slicing Python Strings
# In python we can slide strings into substrings
language = "Python"
first_three = language[0:3]     # Starts at zero index and upto 3 but not including 3
print(first_three)  # Pyt
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Reversing a String
# We can easily reverse strings in python
greeting = "Hello, World!"
print(greeting[::-1])   # !dlroW ,olleH

# Skipping Characters While Slicing
# It is possible to skip characters while slicing by passing step argument to slice method
language = "Python"
pto = language[0:6:2]
print(pto)  # pto

# Strings Methods
# There are many string methods which allow us to format strings. See some of the string methods:

# - capitalize() : Converts the first character of the string to capital letter
challenge = "thirty days of python"
print(challenge.capitalize())   # "Thirty days of python"

# - count() : return occurences of substring in string, count(subtring, start=..., end=...).
# The start is a starting indexing for counting and end is the last index to count
challenge = "thirty days of python"
print(challenge.count("y"))         # 3
print(challenge.count("y", 7, 14))  # 1
print(challenge.count("th"))        # 2

# - endswith() : Chekcs if a string ends with a specific ending
challenge = "thirty days of python"
print(challenge.endswith("on"))     # True
print(challenge.endswith("tion"))   # False

# - expandtabs() : Replace tab character with spaces, default tab size is 8. It takes tab size argument
challenge = "thirty days of python"
print(challenge.expandtabs())   # "thirty   days   of   python"
print(challenge.expandtabs(10)) # "thirty     days     of     python"

# - find() : Returns the index of the first occurrence of a substring, if not found, returns -1
challenge = "thirty days of python"
print(challenge.find("y"))  # 5
print(challenge.find("th")) # 0 

# - rfind() : Returns the index of the last occurrence of a substring, if not found, returns -1
challenge = "thirty days of python"
print(challenge.rfind("y"))     # 16
print(challenge.rfind("th"))    # 17

# - format() : formats string into a nicer output
first_name = "Theodore Lucky"
last_name = "Tendy"
age = 21
job = "intern"
country = "Taiwan"
sentence = "I am {} {}. I am an {}. I am {} years old. I live in {}.".format(first_name, last_name, age, job, country)
print(sentence)
# I am Theodore Lucky Tendy, I am 21 years old. I am an intern, I live in Indonesia

radius = 10
pi = 3.14
area = pi * radius ** 2
result = "The area of a circle with radius {} is {}".format(str(radius), str(area))
print(result)
# The area of a circle with radius 10 is 314

# - index() : Returns the lowest index of a substring, additional arguments indicate
# starting and ending index (defualt 0 and string length -1). If the substring is not found it raises valueEror
challenge = "thirty days of python"
sub_string = "da"
print(challenge.index(sub_string))      # 7
#print(challenge.index(sub_string, 9))   # error

# - rindex() : Returns the highest index of a substring, additional arguments indicate 
# the starting and ending index (default 0 and string length -1)
challenge = "thrity days of python"
sub_string = "da"
print(challenge.rindex(sub_string))     # 8
#print(challenge.rindex(sub_string, 9))  # error

# - isalnum() : Checks alphanumeric characters
challenge = "ThirtyDaysPython"
print(challenge.isalnum())  # True

challenge = "30DaysPython"
print(challenge.isalnum())  # True

challenge = "thirty days of python"
print(challenge.isalnum())  # False, space is not an alphanumeric character

challenge = "thirty days of python 2024"
print(challenge.isalnum())  # False

# - isalpha : Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = "thirty days of python"
print(challenge.isalpha())  # False, space is excluded

challenge = "ThirtyDaysPython"
print(challenge.isalpha())  # True

num = "12 3"
print(num.isalpha())        # False

# - isdecimal() : Checks if all characters in a string are decimal (0-9)
num = "12 3"
print(num.isdecimal())      # False, space excluded

decimal = "\u00B2"
print(decimal.isdecimal())  # False

challenge = "30DaysPython"
print(challenge.isdecimal())# False

circle = "314"
print(circle.isdecimal())   # True

# - isdigit() : Checks if all characters in a string are numbers (0-9 and some other unicode characters for numebrs)
challenge = "Thrity"
print(challenge.isdigit())  # False

challenge = "30"
print(challenge)
