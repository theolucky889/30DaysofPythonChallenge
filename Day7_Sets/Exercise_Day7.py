# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercise LVL 1

# 1. Find the length of the set it_companies
companies_length = len(it_companies)
print(companies_length)

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Samsung', 'Xiaomi', 'Viewsonic'])
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.pop()
print(it_companies)

# 5. what is the difference between remove and discard
"""1. remove() = when you use the remove method and the element
doesn't exist in the set, Python will raise a 'KeyError' exception.
This behavior is useful when it's important for your program to
know that the removal failed due to the absence of the element"""
my_set = {'apple', 'banana', 'cherry'}
my_set.remove('banana') # Removes 'banana'
# if you try to remove 'banana' again, it will raise KeyError
# my_set.remove('banana') # Raise KeyError

"""2. discard() = does not raise an exception if the element is
not present in the set. It simply does nothing, which can be useful
when it's okay for the element to not exist, and you want to avoid
handling exceptions."""
my_set = {'apple', 'banana', 'cherry'}
my_set.discard('banana')    # removes 'banana'
# Discarding 'banana' again will not raise an error
my_set.discard('banana')    # does nothing, no error\

# Exercise Level 2

# 1. Join A and B
ab = A.update(B)
print(ab)

# 2. Find A intersection B
intersection = A.intersection(B)
print(intersection)

# 3. Is A subset of B
subset = A.issubset(B)
print(subset)

# 4. Are A and B disjoint sets
disjoint_set = A.isdisjoint(B)
print(disjoint_set)

# 5. Join A with B and B with A
union_ab = A.union(B)
print(union_ab)

# 6. What is the symmetric difference between A and B
symmetric_ab = A.symmetric_difference(B)
print(symmetric_ab)

# 7. Delete the sets completely
del A
del B
# print(A)
# print(B)

# Exercise Level 3
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_lst = list(age)
comparison = len(age_lst) == len(age_lst)
print(comparison)

# 2. Explain the differences between the following data types:
"""
- string
-- A string is a sequence of characters enclosed in quotes
-- Strings are immutable, meaning once a string is created, the characters within it cannot be change
-- You can access individual characters of a string using indexing and range of characters using slicing
-- Strings have a variety of methods that allow you to manipulate the text, such as upper(), lower(), split(), etc
Example:
"""
my_string = "Hello, World!"

"""
- list
-- List is an ordered collection of items which can be of different data types
-- Lists are mutable, meaning you can modify their contents
-- Lists support indexing and slicing to access and modify elements
-- Lists have methods like append(), remove(), pop(), etc
Example:
"""
my_list = [1, "Hello", 3.14, True]

"""
- tuple
-- Tuple is similar to a list, its an ordered collection of items, but it is immutable
-- Once a tuple is created, it cannot be modified
-- Tuples also support indexing and slicing to access the elements
-- Tuples are typically used for data that shouldn't change after the tuple is created
Example:
"""
my_tuple = {1, "Hello", 3.14, False}

"""
- set
-- Set is an unordered collection of unique items. Meaning it does not allow duplicate elements
-- Sets are mutable, you can add or remove items, but the items themselves must be mutable
-- Sets do not support indexing or slicing because they are unordered
-- Sets are useful for operations like unions, intersections, and set differences, and for chekcing memberships and eliminating duplicate entries
Example:
"""
my_set = {1, 2, 3, 4, 5}

#3. I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
number_of_unique_words = len(unique_words)
print(number_of_unique_words)