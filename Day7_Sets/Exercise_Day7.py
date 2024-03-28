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
print(A)
print(B)

# Exercise Level 3
