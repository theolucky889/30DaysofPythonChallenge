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
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3?", 'item3' in st)

# Example:
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits)

# Adding Items to a set
# Once a set is created, we cannot change any items and we can also add additional items.

# - Add one item using add()
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')

# Example:
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)

# - Add multiple items using update(). THe update() allows to add multiple items to a set.
# The update() takes a list argument
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5', 'item5', 'item6']) 

# Example:
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)
print(fruits)

