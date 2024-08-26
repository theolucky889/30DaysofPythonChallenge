# HIGHER ORDER FUNCTIONS
"""
In Python functions are treated as first class citizens, allowing us to perform the following operations on functions:
- A function can take one or more function as parameters
- A function can be returned as a result of another function
- A function can be modified
- A function can be assigned to a variable

This section will cover:
1. Handling functions as parameters
2. Returning functions as return value from another functions
3. Using python closures and decorators    
"""

# Function as a Parameter
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :(((

def higher_order_function(f, lst):  # a function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)   # 15


# Function as a Return Value
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)
    
def higher_order_function(type):
    if type == 'square':
        return square
    if type == 'cube':
        return cube
    if type == 'absolute':
        return absolute
    
result = higher_order_function('square')
print(result(3))    # 9
result = higher_order_function('cube')
print(result(3))    # 27
result = higher_order_function('absolute')
print(result(-3))   # 3

# as we can see from the above example that the higher order function is returning different functions depending on the passed parameter

# Python Closures

"""
Python allows a nested function to access the outer scope of the enclosing function. This is known as a Closure.
In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function
"""

# Example
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add
closure_result = add_ten()
print(closure_result(5))    # 15
print(closure_result(10))   # 20

# Python Decorators
"""
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying
its structure. Decorators are usually called before the definition of a function you want to decorate.
"""

# Creating Decorators
"""
To create a decorator function, we need an outer function with an inner wrapper function
"""

# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())  # WELCOME TO PYTHON

# Implement the example above using decorator
'''This decorator function is a higher order function that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

# Accepting Parameters in Decorator Functions
'''
Most of the time we need our functions to take parameters, so we might need to define a decorator that accepts parameters
'''

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to learn.".format(first_name, last_name, country))

print_full_name("Theodore Lucky", "Tendy", "Taiwan")