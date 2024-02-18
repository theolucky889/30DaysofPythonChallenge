#   Comments
#This is the first comment
#This is the second comment
#Python is eating the world

"""Multi Line Comment
Multi line comment takes multiple lines.
Python rocks 
"""

#Data types

#Numbers
# - Integers(Zero, Negative Numbers, Positive Numbers): -3, -1, 0, 1, 34
# - Float (Decimal Numbers): -3.5, 0.0, 0.1
# - Complex Numbers: 1 + 2j, 2 + j

#Strings (A collection of one or more characters under a single or double quote. If a string has more than one sentence then we use a triple quote)
# 'Asabeneh'
# 'Finland'
# 'Python'
# 'I love learning'
# 'I hope that I will enjoy learning python with 30DaysOfPython Challenge'

#Booleans (A boolean data type is either a True or False value. T and F should always be uppercase)
# True
# False

#List (Python list is an ordered collection which allows to store different data type items. A list is similar to an array in JS)
# [0, 1, 2, 3, 4. 5] #All same data types
# ['Banana', 'Orange', 'Mango', 'Avocado'] #All the same data types
# ['Finland', 'Estonia', 'Indonesia', 'Taiwan'] #All the same data types
# ['Banana', 10, False, 9.18] #List can also have different data  types

#Dictionary (Dictionary object is an unordered collection of data in a key value pair format)
"""
{
'first_name':'Lucky',
'last_name':'Tendy',
'country':'Indonesia',
'age':22,
'is_married':False,
'skills':['Python', 'JS', 'React', 'CSS']
}
"""

#Tuple (Tuple is an ordered collection of different data type like list but tuples cannot be modified once they are creatued, They are immutable)
# ('Lucky', 'Joesline', 'Vincent', 'Edison') #Names
# ('Earth', 'Venus', 'Jupiter', 'Mercury', 'Saturn', 'Uranus') #Planets

# Set (Set is a collection of data types similar to list and tuple. Unlike list and typle, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items)
# {2, 4, 3, 5}
# {3.14, 9.81, 2.7} #Order is not important in a set

#Day 1 - 30DaysOfPython

print(2 + 3)    #Addition
print(3 - 1)    #Subtraction
print(2 * 3)    #Multiplication
print(3 / 2)    #Division
print(3 ** 2)   #Exponential
print(3 % 2)    #Modulus
print(3 // 2)   #Floor division operator

#Checking data types
print(type(10))                     #Int
print(type(3.14))                   #Float
print(type(1 + 3j))                 #Complex Number
print(type('Theodore'))             #String
print(type([1, 2, 3]))              #List
print(type({'name':'Theodore'}))    #Dictionary
print(type({9.8, 3.14, 2.7}))       #Set
print(type([9.8, 3.14, 2.7]))       #Tuple

#Find an Euclidian Distance between (2,3) and (10,8)
import math

p = [2, 3]
q = [10, 8]

#Calculate Euclidian Distance
print(math.dist(p, q))



