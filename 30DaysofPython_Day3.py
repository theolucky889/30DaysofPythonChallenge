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
density = mass / volume     # 1000 Kg/m^34
print(density, 'Kg/m^3')
