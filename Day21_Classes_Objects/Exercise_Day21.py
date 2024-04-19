# Day 21 Classes and Objects (jumped from day 11 to 21, will do 12-20 when have time)

# Classes and Objects
"""
Python is an object oriented programming language. Everything in Python is an object, with its
properties and methods. A number, string, list, dictionary, tuple, set, etc. used in a program
is an object of a corresponding built-in class. We create class to create an object. A class
is like an object constructor, or a 'blueprint' for creating objects. We instantiate a class to
create an object. The class defines attributes and the behaviour of the object, while the object
on the other hand, represents the class

We have been working with classes and objects right from the beginning of this challenge.
Every element in a Python program is an object of a class.
"""

# Creating a class
# To create a class we need the keyword 'class' followed by the name and colon. Class name should be CamelCase.

# syntax
'''
class ClassName:
    code goes here
    '''
# Example
class Person:
    pass
print(Person)   # <__main__.Person object at 0x10804e510>

# Creating an Object
# We can create an object by calling the class
p = Person()
print(p)