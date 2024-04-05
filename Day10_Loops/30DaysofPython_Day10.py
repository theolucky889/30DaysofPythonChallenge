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
