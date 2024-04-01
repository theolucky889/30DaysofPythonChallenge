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
if your_age > 22:
   if my_age - your_age == 1:
       print(f"You are {my_age - your_age} year older than me")
    else:
        print(f"You are {my_age - your_age} years older than me")
if your_age < 22:
    if your_age - my_age == 1:
        print(f"You are {your_age - my_age} year younger than me")
    else:
        print(f"You are {your_age - my_age} years older than me")
elif my_age == your_age:
    print("We have the same age")

    