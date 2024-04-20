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

# Class Constructor
'''
In the examples above, we have created an object from the Person class. However, a class without
a constructor is not really useful in real applications. Let us use constructor function to make
our class more useful. Like the constructor function in Java or JavaScript. Python has also 
built-in init() construction function. the init constructor function has self parameter
which is a reference to the current instance of the class
Example:
'''
class Person:
    def __init__(self, name):
        # self allows to attach parameter to the class
        self.name = name
        
p = Person('Lucky')
print(p.name)
print(p)

# output
'''
Lucky
<__main__.Person object at 0x00000295C755B1A0>
'''