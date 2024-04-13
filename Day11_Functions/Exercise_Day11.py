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

