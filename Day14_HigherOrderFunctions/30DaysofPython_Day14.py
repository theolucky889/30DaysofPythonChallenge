# HIGHER ORDER FUNCTIONS
"""
In Python functions are treated as first class citizens, allowing us to perform the following operations on functions:
- A function can take one or more function as parameters
- A function can be returned as a result of another function
- A function can be modified
- A function can be assigned to a variable

This section will cover:
1. Handling functions as parameters
2. Returning functions as return value from another functions
3. Using python closures and decorators    
"""

# Function as a Parameter
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :(((

def higher_order_function(f, lst):  # a function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)   # 15

