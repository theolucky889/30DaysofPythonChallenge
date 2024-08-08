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
print(numbers)      # [(0, 0), (1, 1,), (2, 4), (3, 9), (4, 16), (5, 25)]

# example 3
# list comprehension can be combined with if expression

# generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]     # to generate even numbers list in range 0 to 20
print(even_numbers)     # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# generatingg off numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]      # to generate odd numbers list in range 0 to 20
print(odd_numbers)      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# filter numbers: filters out positive even numbers from the list below