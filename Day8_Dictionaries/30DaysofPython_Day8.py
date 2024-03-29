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
