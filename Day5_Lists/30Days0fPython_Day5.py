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
