# Dictionaries
# A dictionary is a collection of unordered, modifiable(mutable) paried (key: value) data type

# Creating a Dictionary
# To create a dictionary we use curly brackers, {} or the dict() built-in function

# syntax
empty_dixt = {}

# Dictionary with data values
dct = {'key1':'value`1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# Example:
person = {
    'first_name':'Theodore Lucky',
    'last_name':'Tendy',
    'age':22,
    'country':'Indonesia',
    'is_married':False,
    'skills':['Python', 'HTML/CSS', 'JS', 'React'],
    'address':{
        'street':'Taiyuan Street',
        'zipcode':103
        
    }
}
# the dictionary above shows that a value could be any data types

# Dictionary length
# it checks the number of 'key:value' pairs in the dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct))

# Example:
person = {
    'first_name':'Theodore Lucky',
    'last_name':'Tendy',
    'age':22,
    'country':'Indonesia',
    'is_married':False,
    'skills':['Python', 'HTML/CSS', 'JS', 'React'],
    'address':{
        'street':'Taiyuan Street',
        'zipcode':103
        
    }
}
print(len(person))

# Accessing Dictionary Items
# We can access Dictionary items by referring to its key name

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1'])
print(dct['key4'])

# Example:
person = {
    'first_name':'Theodore Lucky',
    'last_name':'Tendy',
    'age':22,
    'country':'Indonesia',
    'is_married':False,
    'skills':['Python', 'HTML/CSS', 'JS', 'React'],
    'address':{
        'street':'Taiyuan Street',
        'zipcode':103
    }
}
print(person['first_name'])
print(person['country'])
print(person['skills'])
print(person['skills'][1])
print(person['address'])
print(person['address']['street'])
# print(person['city'])   # Error

"""Accessing an item by key name raises an error if the key does not exist.
To avoid this error, first we have to check if a key exist or we can use the get method.
The get method returns None, which is a NoneType object data type, if the key does not exist"""
person = {
    'first_name':'Theodore Lucky',
    'last_name':'Tendy',
    'age':22,
    'country':'Indonesia',
    'is_married':False,
    'skills':['Python', 'HTML/CSS', 'JS', 'React'],
    'address':{
        'street':'Taiyuan Street',
        'zipcode':103
    }
}
print(person.get('first_name'))
print(person.get('country'))
print(person.get('skills'))
print(person.get('city'))   # None

# Adding Items to a Dictionary
# We can add new key and value pairs to a dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'

# Example:
person = {
    'first_name':'Theodore Lucky',
    'last_name':'Tendy',
    'age':22,
    'country':'Indonesia',
    'is_married':False,
    'skills':['Python', 'JS', 'HTML/CSS', 'React'],
    'address':{
        'street':'Taiyuan Street',
        'zipcode':103,
    }
}
person['job_title'] = 'Intern'
person['skills'].append('Selenium')
print(person)

# Modifying items in a dictionary
# We can modify items in a dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'

# Example:
person = {
    'first_name':'Theodore Lucky',
    'last_name':'Tendy',
    'age':22,
    'country':'Indonesia',
    'is_married':False,
    'skills':['Python', 'JS', 'HTML/CSS', 'React'],
    'address':{
        'street':'Taiyuan Street',
        'zipcode':103
    }
}
person['first_name'] = 'boy'
person['age'] = 223
print(person)

# Checking Keys in a Dictionary
# We use the in operator to check if a key exist in a dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct)    # True
print('key5' in dct)    # False

# Removing Key and Value Pairs from a Dictionary
"""
- pop(key): removes the item with the specified key name:
- popitem(): removes the last item
- del: removes an item with specified key name
"""

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1')     # remove key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem()   # removes the last item
del dct['key2']

# Example:
person = {
    'first_name':'Theodore Lucky',
    'last_name':'Tendy',
    'age':22,
    'country':'Indonesia',
    'is_married':False,
    'skills':['Python', 'JS', 'HTML/CSS', 'React'],
    'address':{
        'street':'Taiyuan Street',
        'zipcode':103
    }
}
person.pop('first_name')
person.popitem()
del person['country']

# Changing Dictionary to a list of items
# the items() method changes dictionary to a list of tuples

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())
# dct_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# Clearing a dictionary
# if we don't want the items in a dictionary we can clear them using clear() method

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear())  # None

# Deleting a Dictionary
# if we do not use the dictionary we can delete it completely

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

# Copy a dictionary
# We can copy a dictionary using copy() method. Using copy we can avoid mutation of the original dictionary

# synatx
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
print(dct_copy)

# Getting Dictionary keys as a list
# keys() method gives us all the keys of a dictionary as a list

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

# Getting Dictionary values as a list
# The values() method gives us all the values of a dictionary as a list

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)
