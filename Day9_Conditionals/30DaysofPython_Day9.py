# Conditionals
"""
By default, statements in Python script are executed sequentially from top to bottom. If the 
processing logic require so, the sequential flow of execution can be altered in two ways:
- Conditional Execution: a block of one or more statements will be executed if a certain expression is true
- Repetitive Execution: a block of one or more statements will be repetitively executed as long as 
  a certain expression is true.
In this section, we will cover if, else, elif statements. The comparison and logical operators
we learned in previous sections will be useful here
"""

# If condition
# In python and other programming languages the key word if is used to check if a condition
# is true and to execute the block code. ALWAYS REMEMBER THE INDENTATION AFTER THE COLON

# # syntax
""" if condition:
    this part of code runs for truthy conditions"""

# Example: 1
a = 3
if a > 0:
    print('A is a positive number')
    
"""
As you can see in the example above, 3 is greater than 0. The condition was true and the block
code was executed. However, if the condition is false, we will not see the result.
In order to see the result of the false condition, we should have another block, which is else
"""

# If Else
# If condition is true, the first block will be executed, if not, the else condition will run

# syntax
"""if condition:
    this part of the code runs for truthy conditions
else:
    this part of the code runs for false conditions"""
    
# Example:
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
# THe condition above proves false, therefore the else block was executed.

# How about if our condition is more than two? We can use __elif__

# if elif else
"""
In our daily life, we make decision on daily basis. We make decision not by checking one or
two conditions but multiple conditions. As similar to life, programming is also full of conditions.
We use elif when we have multiple conditions
"""
# syntax
"""
if condition:
    code
elif condition:
    code
else:
    code
"""
# Example
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# Short hand

# syntax
"""
code if condition else code
"""
# Example
a = 3
print('A is positive') if a > 0 else print('A is negative') # if first condition is met, 'A is positive' will be printed

# Nested Conditions
# Conditions can be nested

# syntax
"""
if condition:
    code
    if condition:
    code
"""
# Example
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive numnber')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
# WE can avoid writing nested condition by using logical operator and

# If condition and logical operators

# syntax
"""
if condition and condition:
    code
"""

# Example
a = 0
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# If and Or Logical Operators

# syntax
"""
if condition or condition:
    code
"""
# Example:
user = 'Theodore'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access Granted!')
else:
    print('Access Denied!')


