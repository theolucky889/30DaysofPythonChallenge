# Sets
"""Set is a collection of items. The mathematics definition of setes
can also be applied in Python. Set is a collection of unordered
and un-indexed distinct elements. In Python, set is used to store
unique items, and it is possible to find the union, intersection,
difference, symmetric difference, subset, super set and disjoint set among sets"""

# Creating a Set
# We use the set() built-in function

# - Creating an empty set
st = set()

# - Creating a set with initial items
st = {'item1', 'item2', 'item3', ' item4'}

# Example
fruits = {'banana', 'orange', 'mango', 'lemon'}

# Getting Set's length
# we use len() method to find the length of a set
st = {'item1', 'item2', 'item3', 'item4'}
len(st)

# Example:
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits_length = len(fruits)
print(fruits_length)

# Accessing items in a set
# We use loops to access items

# Checking an Item
# To check if an item exist in a list, we use in membership operator
