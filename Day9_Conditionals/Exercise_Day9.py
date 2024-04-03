# Exercise Level 1
# 1. Get user input using ("Enter your age: "). If a user is 18 or older, give feedback:
# you are old enough to drive. If below 18, give feedback to wait for the missing amout of years.
# output
"""
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age:
You need 3 more years to learn to drive
"""
user_input = int(input("Enter your age: "))
too_young = 18 - user_input
if user_input >= 18:
    print("You are old enough to learn to drive")
else:
    print(f"You need {too_young} more years to learn to drive")
    
# 2. Compare the values of my_age and your_age using if ... else. Who is older(me or you)?
# Use input("Enter your age: ") to get the age as input. You can use a nested condition to print
# 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text
# if my_age = your_age.
# Output:
"""
Enter your age: 30
You are 5 years older than 5
""" 
my_age = 22
your_age = int(input("Enter your age: "))
if your_age > my_age:
    age_diff = your_age - your_age
    if age_diff == 1:
       print(f"You are {your_age - your_age} year older than me")
    else:
        print(f"You are {your_age - your_age} years older than me")
elif your_age < my_age:
    age_diff = my_age - your_age
    if age_diff == 1:
        print(f"You are {my_age - your_age} year younger than me")
    else:
        print(f"You are {my_age - your_age} years younger than me")
else:
    print("We have the same age")

# 3. Get two numbers from the user using input prompt. If a is greater than b, return 
# a is greater than b, if a is less than b, return a is smaller than b, else a is equal to b
# Output:
"""
Enter number one: 4
Enter number two: 3
4 is greater than 3
"""
number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))
if number_one > number_two:
    print(f"{number_one} is greater than {number_two}")
elif number_one < number_two:
    print(f"{number_two} is greater than {number_one}")
else:
    print(f"{number_one} is equal to {number_two}")
    
# Exercise Level 2

# 1. Write a code which gives grade to students according to their scores:
"""
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""
grading_score = int(input("Please Enter your score in numbers: "))
if 80 <= grading_score <= 100:
    print("A")
elif 70 <= grading_score <= 89:
    print("B")
elif 60 <= grading_score <= 69:
    print("C")
elif 50 <= grading_score <= 59:
    print("D")
else:
    print("F")
    
# 2. Check if the season is Autumn, Winter, Spring or summer. If the user input is:
# september, october, november, the season is autumn
# December, january, february is winter
# march, april, may is spring
# June, july, august is summer
month_seasons = input("Enter a month: ").lower()
if month_seasons == 'september' or month_seasons == 'october' or month_seasons == 'november':
    print("Autumn")
elif month_seasons == 'december' or month_seasons == 'january' or month_seasons == 'february':
    print("Winter")
elif month_seasons == 'march' or month_seasons == 'april' or month_seasons == 'may':
    print("Spring")
elif month_seasons == 'june' or month_seasons == 'july' or month_seasons == 'august':
    print("Summer")
else: 
    print("Invalid Month")

# 3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruits doesn't exist in the list, add the fruit to the list and print the modified list
# IF the fruits exists print('That fruit already exist in the list')
fruit_input = input("Enter a fruit: ")
if fruit_input == fruits:
    print("That fruit is already exist in the list")
    print(fruits)
else:
    print(f"{fruit_input} Added to the list")
    fruits.append(fruit_input)
    print("Updated fruit list: ", fruits)