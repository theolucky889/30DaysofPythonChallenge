# Day 11 Functions
# Functions
"""
A function is a reusable block of code or programming statements designed to perform a certain task.
To define or declare a function, Python dovides the def keyword. The following is the syntax for
defining a function. The function block of code is executed only if the function is called or invoked.
"""

# Declaring and calling a function
"""
When we make a function, we call it declaring a function. When we start using the it, we call it
calling or invoking a function. Function can be declared with or without parameters.
"""

# syntax
"""
# Declaring a function
def function_name():
    code
    code
# calling a function
function_name()
"""
# Function without Parameters
# Function can be declared without parameters

# example:
def generate_full_name():
    first_name = 'Theodore Lucky'
    last_name = 'Tendy'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name()

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

# Function with parameters
"""
In a function, we can pass different data types(numbers, string, boolean, list, tuple, dictionary or set) as a parameter
"""
# - Single Parameter: if our function takes a parameter, we should call our function with an argument

# syntax
# Declaring a function
"""
def function_name(parameter):
    codes
    codes

# Calling function
print(function_name(argument))
"""
# Example
def greetings(name):
    message = name + ', welcome to Python for Everyone'
    return message

print(greetings('Theodore'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle(r):
    PI = 3.14
    area = PI * r * r
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# - Two Parameter: 
"""
A function may or may not have a parameter or parameters. A function may also have two or more
parameters. If our function takes parameters, we should call it with arguments. 
"""