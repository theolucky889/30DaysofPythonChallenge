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

