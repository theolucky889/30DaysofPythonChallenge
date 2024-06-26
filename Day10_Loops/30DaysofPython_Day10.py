# LOpps
"""
Life is full of routines. In programming we also do lots of repetitive tasks. In order to handle
repetitive tasks, programming languages use loops. Python programming language also provides
the following types of two loops:
1. while loop
2. for loop
"""

# While loop
"""
We use the reserved word while to make a while loop. It is used to execute a block of statements
repeatedly until a given condition is satisfied. When the condition becomes false, the lines
of code after the loop will be continued to be executed
"""

# syntax
"""
while condition:
      code goes here
"""

# Example:
count = 0
while count < 5:
    print(count)
    count = count + 1
# prints from 0 to 4
"""
In the above while loop, the condition becomes false when count is 5. That is when the loop stops.
If we are interested to run block of code once the condition is no longer true, we can use else.
"""

# syntax
"""
while condition:
    code goes here
else:
    code goes here
"""

# Example:
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
# the above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement. 5 will be printed

# Break and Continue - Part1
# - Break: we use break when we like to get out of or stop the loop.

# syntax
"""
while condition:
    code goes here
    if another_condition:
        break
"""

# Example
count = 0 
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
# The above while loop only prints 0, 1, 2. It will stop when it reaches 3

# - Continue: With the continue statement, we can skip the current iteration, and continue with the next:

# syntax
"""
while condition:
    code goes here
    if another_condition:
        continue
"""    

# Example:
count = 0 
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
# The above while loop only prints 0, 1, 2 and 4 (skips 3)

# For loop
"""
A for keyword is used to make a for loop, similar with other programming languages, but with some
syntax differences. Loop is used for iterating over a sequence(that is either a list, a tuple,
a dictionary, a set or a string)
"""
# - For loop with list

# syntax
"""
for iterator in lst:
    code goes here
"""
# Example
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:  # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
    
# - for loop with string

# syntax
"""
for iterator in string:
    code goes here
"""    

# Example:
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

# - for loop with tuple

# syntax
"""
for iterator in tpl:
    code goes here
"""

# Example:
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# - for loop with dictionary looping through a dictionary gives you the key of the dictionary

# syntax
"""
for iterator in dct:
    code goes here
"""

# Example
person = {
    'first_name':'Theodore Lucky',
    'last_name':'Tendy',
    'age':22,
    'country':'Taiwan',
    'is_married':False,
    'skills':['Python', 'Selenium', 'JavaScript', 'React'],
    'address':{
        'street':'TaiYuan Street',
        'zipcode':103
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)

# - Loops in set

# syntax
"""
for iterator in st:
    code goes here
"""

# Example
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'Viewsonic', 'Amazon'}
for company in it_companies:
    print(company)

# Break and Continue Part2
# short reminder: Break: WE use break when we like to stop our loop before it is completed

# syntax
"""
for iterator in sequence:
    code goes here
    if condition:
        break
"""

# Example:
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        break
# The loop stops when it reaches 3

# Continue: We use continue when we like to skip some of the steps in the iteration of the loop

# syntax
"""
for iterator in sequence:
    code goes here
    if condition:
        continue
"""
# Example:
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
    print('outside the loop')
    # If the number equals 3, the step after the condition(but inside the loop) is skipped and the execution of the loop continues if there are any iterations left
    
# The range function
"""
The range() function is used for a list of numbers. THe range(start, end, step) takes three
parameters: starting, ending and increment. By default it starts from 0 and the increment is 1
The range sequence needs at least 1 argument(end).
Creating sequences using range
"""
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))  # 2 arguments indicate start and end of the sequence, step set to default 1
print(st)   # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0, 11, 2))
print(lst)  # [0, 2, 4, 6, 8, 10]
st = set(range(0, 11, 2))
print(st)   # {0, 2, 4, 6, 8, 10}

# syntax
""" for iterator in range(start, end, step): """

# Example
for number in range(11):
    print(number)   # prints 0 to 10, not including 11

# Nested for loop
# we can write loops inside a loop

# syntax
"""
for x in y:
    for t in x:
        print(t)
"""

# Example:
person = {
    'first_name':'Theodore Lucky',
    'last_name':'Tendy',
    'age':22,
    'country':'Taiwan',
    'is_married':False,
    'skills':['Python', 'Selenium', 'JavaScript', 'React'],
    'address':{
        'street':'TaiYuan Street',
        'zipcode':103
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# For Else
# IF we want to execute some message when the loop ends, we use else.

# syntax
"""
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
"""
# Example:
for number in range(11):
    print(number)
else:
    print('The loop stops at', number)
    
# Pass
"""
In python, when statement is required(after semicolon), but we don't like to execute any code,
we can write the word pass to avoid erros. Also we can use it as a placeholder, for future statements
"""
# Example:
for number in range(6):
    pass