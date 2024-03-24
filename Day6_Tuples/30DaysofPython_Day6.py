# TUPLES
"""
A tuple is a collection of different data types which is ordered and unchangeable(immutable).
Tuples are written with round brackets (). Once a tuple is created, we cannot change its values.
We cannot use add, insert, remove methods in a tuple because it is not modifiable(mutable).
Unlike list, tuple has few methods.
- tuple(): to create an empty tuple
- count(): to count the number of a specified item in a tuple
- index(): to find the index of a specified item in a tuple
- operator(): to join two or more tuples and create a new tuple
"""
# Creating a Tuple
# - Empty a tuple: Creating an empty tuple
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

# Tuple with initial values
# syntax
tpl = ("item1", "item2", "item3")
fruits = ("banana", "orange", "mango", "lemon")

# Tuple length
# we use the len() method
# syntax
tpl = ("item1", "item2", "item3")
len(tpl)

# Accessing Tuple Items
# - Positive indexing similar to the list data types we use positive or negative indexing to access tuple items

# Syntax
tpl = ("item1", "item2", "item3")
first_item = tpl[0]
second_item = tpl[1]

fruits = ("banana", "orange", "mango", "lemon")
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Negative indexing
# negative indexing means beginning from the end, -1 refers to the last item, -2 second last.
# and the negative of the list/tuple length refers to the first item

# syntax
tpl = ("item1", "item2", "item3", "item4")
first_item = tpl[-4]
second_item = tpl[-3]

fruits = ("banana", "orange", "mango", "lemon")
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

# Slicing Tuples
"""
We can slice out a sub-tuple by specifying a range of indexes where to start and where to end
in the tuple, the return value will be a new tuple with specified items.
"""

# - Range of positive indexes
# syntax
tpl = ("item1", "item2", "item3", "item4")
all_items = tpl[0:4]        # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3] # does not include item at index 3

fruits = ("banana", "orange", "mango", "lemon")
all_fruits = fruits[0:4]        # all fruits
all_fruits = fruits[0:]         # all fruits
orange_mango = fruits[1:3]      # does not include item at index 3
orange_to_the_rest = fruits[1:] 

# - Range of negative indexes
# syntax
tpl = ("item1", "item2", "item3", "item4")
all_items = tpl[-4:]            # all items
middle_two_items = tpl[-3:-1]   # does not include item at index 3 (-1)

fruits = ("banana", "orange", "mango", "lemon")
all_items = fruits[-4:]         # all items
orange_mango = fruits[-3:-1]    # does not include item at index 3 (-1)
orange_to_the_rest = fruits[-3:]

# Changing tuples to lists
"""
We can change tupels to lists and lists to tuples. Tuple is immutable if we want to modify
a tuple we should change it into a list
"""
# syntax
tpl = ("item1", "item2", "item3", "item4")
lst = list(tpl)

fruits = ("banana", "orange", "mango", "lemon")
fruits = list(fruits)
fruits[0] = "apple"
print(fruits)               # ["apple", "orange", "mango", "lemon"]
fruits = tuple(fruits)
print(fruits)               # ("apple", "orange", "mango", "lemon")

# Checking an item in a Tuple
"""
We can check if an item exists or not in a tuple using in, it returns a boolean.
"""
# syntax
tpl = ("item1", "item2", "item3", "item4")
"item2" in tpl  # True

fruits = ("banana", "orange", "mango", "lemon")
print("orange" in fruits)   # True
print("apple" in fruits)    # False
# fruits[0] = "apple"     # TypeError: 'tuple' object does not support item assignment

# Joining Tuples
"""We can join two or more tuple using + operator"""

# syntax
tpl1 = ("item1", "item2", "item3")
tpl2 = ("item4", "item5", "item6")
tpl3 = tpl1 + tpl2

fruits = ("banana", "orange", "mango", "lemon")
vegetables = ("Tomato", "Potato", "Cabbage", "Onion", "Carrot")
fruits_and_vegetables = fruits + vegetables\

# Deleting Tuples
"""
IT is not possible to remove a single item in a tuple but it is possible to delete the tuple 
itself using del
"""

# syntax
tpl1 = ("item1", "item2", "item3")
del tpl1

fruits = ("banana", "orange", "mango", "lemon")
del fruits