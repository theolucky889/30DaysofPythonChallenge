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

# syntax
# Declaring a function
"""
def function_name(para1, para2):
    codes
    codes
# Calling a function
print(function_name(arg1, arg2))
"""
# Example:
def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Theodore Lucky', 'Tendy'))

def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(4, 9))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print('Your age is: ', calculate_age(2024, 2002))

def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + ' N'  # The value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

# Passing Arguments with Key and Value

# syntax
# Declaring a function
"""
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe'))     # the order of arguments does not matter
"""

# Example
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    return full_name
print(print_fullname(firstname = 'Theodore Lucky', lastname = 'Tendy'))

def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 5))

# Function Returning a Value Part2
"""
If we do not return a value with a function, then our function is returning None by default.
To return a value with a function, we use the keyword return followed by the variable we are returning.
We can return any kind of data types from a function
"""
# - Returning a string: Example