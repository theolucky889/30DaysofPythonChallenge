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