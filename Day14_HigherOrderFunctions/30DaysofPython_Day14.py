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