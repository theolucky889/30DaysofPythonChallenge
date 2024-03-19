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
first_fruit = fruits[0]
