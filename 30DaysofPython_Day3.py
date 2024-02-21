# Boolean
"""A boolean data type represents one of the two values: True or False. The use of these data
types will be clear once we start using the comparison operator. The first letter T for True
and F for False should be capital unlike JavaScript.
    """
# Example
print(True)
print(False)

# Assignment Operators
"""Assignment operators are used to assign values to variables. Let us take = as an example.
Equal sign in mathematics shows that two values are equal, however in Python it means we are
storing a value in a certain variable and we call it assignment or a assigning value to a
variable.
    """
# Arithmetic Operators:
"""
Addition(+): a + b
Subtraction(-): a - b
Multiplication(*): a * b
Division(/): a / b
Modulus(%): a % b
Floor division(//): a // b
Exponentiation(**): a ** b
    """

# Example: Integers
print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print('Division: ', 4 / 2)  # Division in Python gives floating number
print('Divison: ', 7 / 2)
# Goves result without the floating number or without remainder
print('Division without remainder: ', 7 // 2)
print('Division without remainder: ', 7 // 3)
print('Modulus: ', 3 % 2)  # Modulus = Gives the remainder
print('Exponentiation: ', 2 ** 3)  # Pangkat = 2 pangkat 3 (2 ** 3)

# Example: Floats
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Example: Complex Number
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ', (1 + 1j) * (1 - 1j))

# Example:
# Declaring the variable at the top first
a = 3   # a is a variable name and 3 is an integer data type
b = 2   # b is a variable name and 2 is an integer data type

# Arithmetic operations assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print(total)
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic Operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('Total: ', total)
print('Difference: ', diff)
print('Product: ', product)
print('Division: ', div)
print('Remainder: ', remainder)

# Real Examples
# Calculating area of circle
radius = 10
area_of_circle = 3.14 * radius ** 2
print('Area of a circle: ', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of a rectangle: ', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')  # Adding unit to the weight

# Calculate the density of a liquid
mass = 75   # in KG
volume = 0.075  # in cubic meter
density = mass / volume     # 1000 Kg/m^3
print(density, 'Kg/m^3')

# Comparison Operators
print(3 > 2)    # True, because 3 is greater than 2
print(3 >= 2)   # True, because 3 is greater than 2\
print(3 < 2)    # False, because 3 is greater than 2
print(2 < 3)    # True, because 2 is less than 3
print(2 <= 3)   # True, because 2 is less than 3
print(3 == 2)   # False, because 3 is not equal to 2
print(3 != 2)   # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))   # False
print(len('mango') != len('avocado'))   # True
print(len('mango') <  len('avocado'))   # True
print(len('milk') != len('meat'))       # False
print(len('milk') == len('meat'))       # True
print(len('tomato') == len('potato'))   # True
print(len('python') > len('dragon'))    # False

# Comparing something gives either a True or False
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False: ', False == False)

# In addition to the above comparison operator Python uses:
"""
- is: Returns true if both variables are the same object(x is y)
- is not: Returns true if both variables are not hte same object(x is not y)
- in: Returns True if the queried list contains a certain item(x in y)
- not in: Returns True if the queried list doesn't have a certain item(x not in y)
    """
print('1 is 1', 1 is 1)                     # True, becasue the data values are the same
print('1 is not 2', 1 is not 2)             # True, because 1 is not 2
print('T in Theodore', 'T' in 'Theodore')   # True, T is found in the string
print('E in Theodore', 'E' in 'Theodore')   # False, upper case E is not in the string
print('coding' in 'coding for all')         # True, because coding for all has the word coding
print('a in an:', 'a' in 'an')              # True
print('4 is 2 ** 2', 4 is 2 ** 2)           # True

# Logical Operators 
"""
- and = Returns True if both statements are True
- or = Returns True if one of the statements is True
- not = Reverse the result, returns False if the result is True
    """

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
