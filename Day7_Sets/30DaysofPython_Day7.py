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

# Removing items from a set
"""We can remove an item from a set using remove() method. If
the item is not found, remove() method will raise errors, so
it is good to check if the item exist in the given set.
However, discard() method doesn't raise any errors."""

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

# the pop() method removes a random item from a list and it returns the removed item
# Example
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()    # removes a random item from the set
# If we are interested in the removed item
removed_item = fruits.pop()

# Clearing Items in a set
# If we want to clear or empty the set, we use clear() method

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()

# Example
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)   # set()

# Deleting a set
# If we want to delete the set itself, we can use the del operator

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st

# example
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
# print(fruits)

# Converting a list to a set
# We can convert list to set and set to list. COnverting list to set removes duplicates and only unique items will be reserved

# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)   # {'item2', 'item4', 'item1', 'item3'} - Order is random, because sets in general are unordered
print(st)

# Example: 
fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits = set(fruits)    # {'mango', 'lemon', 'banana', 'orange'}
print(fruits)

# Joining sets
# We can join two sets using the union() or update() method

# - Union(), this method returns a new set

# syntax 
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

# Example
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits_vegetables = fruits.union(vegetables)
print(fruits_vegetables)

# - update(), This method inserts a set into a given set
# syntax 
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)     # st2 contents are added to st1

# Example
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

