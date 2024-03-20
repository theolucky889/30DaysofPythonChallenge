"""
Lists
There are four collection data types in Python: 
- Lists : A collection which is ordered and changeable(modifiable). Allows duplicate members.
- Tuple : A collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members
- Set : A collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set.
        Duplicate members are not allowed
- Dictionary : A collection which is unordered, chengable(modifiable) and indexed. No duplicate members
    """

"""
A list is a collection of different data types which is ordered and modifiable(mutable). A list can be
empty or it may have different data type items.
    """
    
"""
HOW TO CREATE A LIST
    In Python we can create lists in two ways: 
"""

# Using list built-in function
lst = list()
empty_list = list()     # empty list
print(len(empty_list))  # 0

# Using square brackets []
lst = []
empty_list = []         # empty list
print(len(empty_list))  # 0

# List with initial values. We use len() to find the length of the list
fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
animal_products = ["milk", "meat", "butter", "yogurt"]
web_techs = ["HTML", "CSS", "JavaScript", "React", "Redux", "NodeJS", "MongoDB"]
countries = ["Finland", "Estonia", "Denmark", "Sweden", "Norway"]

print("Fruits: ", fruits)
print("Number of fruits: ", len(fruits))
print("Vegetables: ", vegetables)
print("Number of vegetables: ", len(vegetables))
print("Animal Products: ", animal_products)
print("Number of animal products: ", len(animal_products))
print("Web Technologies: ", web_techs)
print("Number of web technologies: ", len(web_techs))
print("Countries: ", countries)
print("Number of countries: ", len(countries))

# Lists can have items of different data types
lst = ["Theodore", 22, True, {"country":"Finland", "city":"Helsinki"}]

# Accessing List Items Using Positive Indexing
# We access each item in a list using their index. A list index starts from 0.
fruits = ["banana", "orange", "mango", "lemon"]
first_fruit = fruits[0]     # accessing the first item using its index
print(first_fruit)          # banana
second_fruit = fruits[1]
print(second_fruit)         # orange
last_fruit = fruits[3]
print(last_fruit)           # lemon

# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing List Items Using Negative Indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item.
fruits = ["banana", "orange", "mango", "lemon"]
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)
print(last_fruit)
print(second_last)

# Unpacking List Items
lst = ["item1", "item2", "item3", "item4", "item5"]
first_item, second_item, third_item, *rest = lst
print(first_item)       # item1
print(second_item)      # item2
print(third_item)       # item3
print(rest)             # ["item4", "item5"]

# First Example
fruits = ["banana", "orange", "mango", "lemon", "lime", "apple"]
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)      # banana
print(second_fruit)     # orange
print(third_fruit)      # mango
print(rest)             # ["lemon", "lime", "apple"]

# Second Example about unpacking list
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

# Third Example about unpacking list
countries = ["Germany", "France", "Belgium", "Sweden", "Denmark", "Finland", "Norway", "Iceland", "Estonia"]
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# Slicing Items from a List
# - Positive indexing: We can specify a range of positive indexes by specifying the start, end and step,
# the return value will be a new list. (default values for start = 0, end = len(lst) - 1(last item), step = 1)
fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[0:4]    # returns all the fruits
# This will also give the same result as the one above
all_fruits = fruits[0:]     # If we don't set where to stop, it takes all the rest
orange_and_mango = fruits[1:3]  # It does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2]  # here we used a 3rd argument, step, it will take every 2nd item - ["banana", "mango"]

# - Negative Indexing : We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list
fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[-4:]    # returns all the fruits
orange_and_mango = fruits[-3:-1]    # it does not include the last index, ["orange", "mango"]
orange_mango_lemon = fruits[-3:]    # this will give starting from -3 to the end, ["orange", "mango", "lemon"]
reverse_fruits = fruits[::-1]       # a negative step will take the list in reverse order, ["lemon", "orange", "mango", "lemon"]

# Modifying lists
# List is a mutable or modifiable ordered collection of items.
fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "avocado"
print(fruits)       # ["avocado", "orange", "mango", "lemon"]
fruits[1] = "apple"
print(fruits)       # ["avocado", "apple", "mango", "lemon"]
last_index = len(fruits) - 1
fruits[last_index] = "lime"
print(fruits)       # ["avocado", "apple", "mango", "lime"]

# Checking Items in a List
# Checking an item if it is a member of a list using in operator
fruits = ["banana", "orange", "mango", "lemon"]
does_exist = "banana" in fruits
print(does_exist)   # True
does_exist = "lime" in fruits
print(does_exist)   # False

# Adding Items to a List
# To add item to the end of an existing list we use the method append()
# syntax
"""
lst = list()
lst.append(item)
"""
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits)           # ["banana", "orange", "mango", "lemon"]
fruits.append("lime")
print(fruits)           # ["banana", "orange", "mango", "lemon", lemon]

# Inserting Items into a List
# We can use insert() method to insert a single item at a specified index in a list.
# Note that other items are shifted to the right. The insert() method takes two arguments: index and an item to insert

# syntax
"""
lst = ["item1", "item2"]
lst.insert(index, item)
"""
fruits = ["banana", "orange", "mango", "lemon"]
fruits.insert(2, "apple")       # insert apple between orange and mango
print(fruits)                   # ["banana", "orange", "apple", "mango", "lemon"]
fruits.insert(3, "lime")        # insert lime between apple and mango
print(fruits)                   # ["banana", "orange", "apple", "lime", "mango", "lemon"]

# Removing Items from a list
# The remove method removes a specified item from a list

# syntax
"""
last = ["item1", "item2"]
lst.remove(item)
"""

fruits = ["banana", "orange", "mango", "lemon", "banana"]
fruits.remove("banana")
print(fruits)               # ["banana", "orange", "mango", "lemon"] this method removes the first occurence of the item in the list
fruits.remove("lemon")
print(fruits)               # ["banana", "orange", "mango"]