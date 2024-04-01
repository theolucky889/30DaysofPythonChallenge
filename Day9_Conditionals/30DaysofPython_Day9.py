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