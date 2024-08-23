# LIST COMPREHENSION
"""
List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list.
List comprehension is considerably faster than processing a list using the for loop    

# syntax
[i for i in iterable if expressionn]
"""

# Example 1
# For instance, if you want to changeg a string to a list of characters. You can use a couple methods.

# way 1
language = 'Python'
lst = list(language)    # changing the string to a list
print(type(lst))        # list
print(lst)              # ['P', 'y', 't', 'h', 'o', 'n']

# second way: list comprehension
lst = [i for i in language]
print(type(lst))    # list
print(lst)          # ['P', 'y', 't', 'h', 'o', 'n']

# example 2
# for instance if you want to generate a list of numbers

# Generating numbers
numbers = [i for i in range(11)]    # to generate numbers from 0 to 10
print(numbers)                      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# it is possible to do mathematical operations during iteration
squares = [i * i for i  in range(11)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)      # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# example 3
# list comprehension can be combined with if expression

# generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]     # to generate even numbers list in range 0 to 20
print(even_numbers)     # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# generatingg off numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]      # to generate odd numbers list in range 0 to 20
print(odd_numbers)      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# filter numbers: filters out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)    # [4, 6, 8, 10]

# flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list =  [number for row in list_of_lists for number in row]
print(flattened_list)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Lambda function
"""
Lambda function is a small anonymous function without a name. it can any number of arguments,
but can only have one expression. lambda function is similar to anonymus functions in JavaScript.
We need it when we when we want to write ananonymous function inside another function
"""
 # creatingg a lambda function
"""
to create a lambda function we use lambda keyword followed by a parameter(s), followed by an expression.
see the syntax and example below.  Lambda function does not use return but it explicitly returns the expression

# syntax
x = lambda param1, param2,  param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
"""

# Example:

# named function
def add_two_nums(a, b):
    return a+ b

print(add_two_nums(2, 3))   # 5

# lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))   # 5

# self invoking lambda function
(lambda a, b: a + b)(2,3)   # 5 - need to encapsulate it in print() to see the result in the console 

square =lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))      # 27

# multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3* b + 4 * c
print(multiple_variable(5, 3, 3)) # 22

# lambda function inside another function
# using a lambda function inside another function
def power(x):
    return lambda n : x ** n

cube = power(2)(3)  # function power now need 2 arguments to run, in seperate rounded brackets
print(cube)         # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)    # 32

