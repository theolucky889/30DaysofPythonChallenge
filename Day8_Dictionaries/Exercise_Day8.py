# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {
        'name':'Edison', 
        'color':'white', 
        'breed':'Pug', 
        'legs':'four', 
        'age':22
}

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city, and address as keys for the dictionary
student = {
    'first_name':'Theodore Lucky',
    'last_name':'Tendy',
    'gender':'male',
    'age':22,
    'marital_status':False,
    'skills':['Python', 'HTML', 'CSS', 'JS'],
    'country':'Taiwan',
    'city':'Taipei',
    'address':{
            'street':'Taiyuan Street',
            'zipcode':103
    }
}

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and chekc the data type (should be a list)
print(type(student['skills']))

# 6. Modify the skills by adding one or two skills
student['skills'].append('React')
print(student)

# 7. Get the dictionary keys as a list
keys = student.keys()
print(keys)

# 8. Get the dictionary values as a list
values = student.values()
print(values)

# 9. Change the dictionary to a list of tuples using items() method
print(student.items())

# 10. Delete one of the items in the dictionary
del student['marital_status']
print(student)

# 11. Delete one of the dictionaries
del student
