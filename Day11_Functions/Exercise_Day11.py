# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def sum_two_numbers(num1, num2):
    total = num1 + num2
    print(total)
sum_two_numbers(3, 4)

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    PI = 3.14
    area = PI * r * r
    print(area)
area_of_circle(9)

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments
# Check if all the list items are number types. If not, give a reasonable feedback
def add_all_nums(*numbers):
    total = 0
    for num in numbers:
        # Check if the item is not a number
        if not isinstance(num, (int, float)):
            return "All items should be numbers"
        total += num
    return total
print(add_all_nums(4, 5, 6, 7, 8))
print(add_all_nums('python', 4, 5, 6, 7.7, '5'))

# 4. Temperature in °Ccan be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def change_temp(temp_cel):
    fah_to_cel = (temp_cel * (9 / 5)) + 32
    return fah_to_cel
print(change_temp(60))

# 5. Write a function called check-season, it takes a month parameter and returns the season:
# Autumn, Winter, Spring, Summer
def season_check(month_param):
    if month_param == 'december' or month_param == 'january' or month_param == 'february':
        return 'Winter'
    elif month_param == 'march' or month_param == 'april' or month_param == 'may':
        return 'Spring'
    elif month_param == 'september' or month_param == 'october' or month_param == 'november':
        return 'Autumn'
    elif month_param == 'june' or month_param == 'july' or month_param == 'august':
        return 'Summer'
    else:
        return 'Invalid Month'

months = input('Select a month: ').lower()
print(season_check(months))

# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(linear_eq):
    rhs = linear_eq.split('=')[1]
    
    if 'x' not in rhs:
        return 0
    slope_part = rhs.split('x')[0].strip()
    
    if slope_part == '' or slope_part =='+':
        return 1
    elif slope_part == '-':
        return -1
    return float(slope_part)

print(calculate_slope('y = 2x + 3'))
print(calculate_slope('y = -x - 5'))
print(calculate_slope('y = x'))
print(calculate_slope('y = 3x + 2'))

# 7. Quadratic Equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return(x1, x2)
    elif discriminant == 0:
        x = -b / (2*a)
        return(x)
    else:
        real_part = -b / (2*a)
        imaginary_part = (abs(discriminant)**0.5) / (2*a)
        return (real_part + imaginary_part*1j, real_part - imaginary_part*1j)
print(solve_quadratic_eqn(1, -3, 2))
print(solve_quadratic_eqn(1, 2, 1))
print(solve_quadratic_eqn(1, 0, 1))

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list
def print_list(lst):
    for element in lst:
        print(element)
    
my_list = [1, 2, 3, 4, 5, 'a', 'b', 'c']
print_list(my_list)

# 9. Declare a function named reverse_list. IT takes an array as a parameter and it returns the reverse of the array(use loops)
'''
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(['A', 'B', 'C']))
# ['C', 'B', 'A']
'''
def reverse_list(arry):
    reversed_array = []
    
    for i in range(len(arry) -1, -1, -1):
        reversed_array.append(arry[i])
    return reversed_array

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(['A', 'B', 'C']))

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_item(cap_lst):
    capitalized_list = []
    for items in cap_lst:
        capitalized_list.append(items.upper())
    return capitalized_list

lst_capital = ['hello', 'python', 'sqa', 'viewsonic']
capitalized_items = capitalize_list_item(lst_capital)
print(capitalized_items)

# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end
'''
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
'''
def add_item(item_add, items):

    item_add.append(items)
    return item_add

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

# 12. Declare a function named remove_item. It takes a list and an item parameter. It returns a list with the item removed from it
'''
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
'''
def remove_item(item_remove, items):
    item_remove.remove(items)
    return item_remove

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range
'''
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
'''
def sum_of_numbers(numbers):
    total = 0
    for num in range(1, numbers + 1):
        total += num
    return total

print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range
def sum_of_odds(odd_number):
    total = 0
    for num in range(1, odd_number + 1):
        if num % 2 == 1:
            total += num
    return total
    
print(sum_of_odds(5))
print(sum_of_odds(10))
print(sum_of_odds(100))

# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range
def sum_of_evens(even_number):
    total = 0
    for num in range(1, even_number + 1):
        if num % 2 == 0:
            total += num
    return total

print(sum_of_evens(5))
print(sum_of_evens(10))
print(sum_of_evens(100))


# Exercise Level 2
# 1. Declare a function named evens_and_odds. It takes a positive integer as parameter and it counts number of evens and odds in the number

def evens_and_odds(numbers):
    total_even = 0
    total_odd = 0
    for num in range(1, numbers + 1):
        if num % 2 == 0:
            total_even += num
        else:
            total_odd += num
    print('The number of odds are ', total_odd)
    print('The number of evens are ', total_even)

evens_and_odds(5)        
evens_and_odds(10)
evens_and_odds(100)

# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(whole_number):
    if whole_number < 0:
        return 'Factorial is not defined for negative numbers'
    if whole_number == 0:
        return 1
    return whole_number * factorial(whole_number - 1)

print(factorial(5))
print(factorial(3))
print(factorial(0))

# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(empty_maybe):
    if empty_maybe in (None, '', [], {}, (), 0):
        return True
    else:
        return False

print(is_empty(""))       
print(is_empty([]))       
print(is_empty({}))       
print(is_empty(0))        
print(is_empty(None))     
print(is_empty("Hello"))  
print(is_empty([1, 2]))

# 4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_varience, calculate_std(standard deviation)
def calculate_mean(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]
    
def calculate_mode(numbers):
    if not numbers:
        return None
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    mode = [k for k, v in frequency.items() if v == max_freq]
    return mode if len(mode) > 1 else mode[0]

def calculate_range(numbers):
    if not numbers:
        return None
    return max(numbers) - min(numbers)

def calculate_variance(numbers):
    if not numbers:
        return None
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_std(numbers):
    if not numbers:
        return None
    return (calculate_variance(numbers)) ** 0.5

data = [10, 12, 23, 23, 16, 23, 21, 16]

print("Mean:", calculate_mean(data))
print("Median:", calculate_median(data))
print("Mode:", calculate_mode(data))
print("Range:", calculate_range(data))
print("Variance:", calculate_variance(data))
print("Standard Deviation:", calculate_std(data))

# Exercise Level 3
# 1. Write a function called is_prime, which chekcs if a number is prime
def is_prime(prime_number):
    if prime_number < 2:
        return False
    
    if prime_number > 2 and prime_number % 2 == 0:
        return False
    
    for i in range(3, int(prime_number ** 0.5) + 1, 2):
        if prime_number % i == 0:
            return False
    return True

print(is_prime(3))
print(is_prime(11))
print(is_prime(4))
print(is_prime(9))
print(is_prime(1))
print(is_prime(87))
print(is_prime(54))

# 2, Write a function which checks if all items are unique in the list
def all_unique(items):
    return len(items) == len(set(items))

print(all_unique([1, 2, 3, 4, 5]))  
print(all_unique([1, 2, 3, 3, 4]))  
print(all_unique(['apple', 'banana', 'cherry']))  
print(all_unique(['apple', 'banana', 'cherry', 'apple']))

# 3. Write a function which checks if all the items of the list are of the same data type
def same_type(items):
    if not items:
        return True
    
    first_type = type(items[0])
    for item in items:
        if type(item) != first_type:
            return False
    return True

print(same_type([1, 2, 3, 4, 5])) 
print(same_type([1, 2, '3', 4, 5]))  
print(same_type(['apple', 'banana', 'cherry']))  
print(same_type([]))  

# 4. Write a function which check if provided variable is a valid python variable
def is_valid_variable(variable_name):
    """
    Check if the provided string is a valid Python variable name without using any imports.

    Args:
    variable_name (str): The string to check for validity as a Python variable name.

    Returns:
    bool: True if the string is a valid Python variable name, False otherwise.
    """
    # Define a list of Python reserved keywords
    keywords = {
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
        'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
    }

    if not variable_name:  # Check if the string is empty
        return False
    if variable_name in keywords:  # Check if the string is a Python keyword
        return False
    if not (variable_name[0].isalpha() or variable_name[0] == '_'):  # Check the first character
        return False
    for char in variable_name[1:]:  # Check remaining characters
        if not (char.isalnum() or char == '_'):
            return False
    return True

# Example usage
print(is_valid_variable('hello'))      # Output: True
print(is_valid_variable('_hello123'))  # Output: True
print(is_valid_variable('2hello'))     # Output: False
print(is_valid_variable('class'))      # Output: False (because it's a keyword)

'''
5. Go to the data folder and access the countries-data.py file.
Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
'''

# Mock data structure as an example
countries = [
    {'name': 'Country A', 'languages': ['English', 'French'], 'population': 50000000},
    {'name': 'Country B', 'languages': ['English', 'Spanish'], 'population': 70000000},
    {'name': 'Country C', 'languages': ['French', 'Arabic'], 'population': 20000000},
    # More countries...
]

def most_spoken_languages(countries, top_n=10):
    language_count = {}
    for country in countries:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += country['population']
            else:
                language_count[language] = country['population']
    sorted_languages = sorted(language_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_languages[:top_n]

def most_populated_countries(countries, top_n=10):
    sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    return [(country['name'], country['population']) for country in sorted_countries[:top_n]]

# Example usage
print(most_spoken_languages(countries, 10))
print(most_populated_countries(countries, 10))
