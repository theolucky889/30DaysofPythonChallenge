# 1. Iterate 0 to 10 using for loop, do the same thing using while loop
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     print(number)

for number in range(11):
    print(number)

number = 0
while number < 11:
    print(number)
    number = number + 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop
for number in range (10, -1, -1):
    print(number)

number = 10
while number >= 0:
    print(number)
    number = number - 1

# 3. Write a loop that makes seven calls to print(), so we get on the output of the following triangle:
"""
#
##
###
####
#####
######
#######
"""
hashtag = '#'
for i in range(7):
    print(hashtag)
    hashtag += '#' 

# 4. Use nested loops to create the following:
"""
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""
hashtag = '#'
for row in range(8):
    row_str = ''
    for col in range(8):
        row_str += hashtag + ' '
    print(row_str)
    
# 5. Print the following pattern:
"""
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""
for i in range(11):
    print(f'{i} x {i} = {i * i}')

# 6. Iterate through the list, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] using a for loop and print out the items
lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for i in lst:
    print(i)

# 7. Use for loop to iteratoe from 0 to 100 and print only the even numbers
for numbers in range(100):
    if numbers % 2 == 0:
        print(numbers)
        
# 8. Use for loop to iterator from 0 to 100 and print only odd numbers
for numbers in range(100):
    if numbers % 2 != 0:
        print(numbers)

# Exercise Level 2
# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers
# The sum of all numbers is 5050
total = 0
for numbers in range(101):
    total += numbers
    print(numbers)
print('the sum of all numbers is', total)

# 2. Use for loop to iterator from 0 to 100 and print the sum of all evens and the sum of all odds
total_even = 0
total_odd = 0
for numbers in range(101):
    if numbers % 2 == 0:
        total_even += numbers
    else:
        total_odd += numbers
print('The sum of all evens is ', total_even)
print('The sum of all odds is ', total_odd)

# Exercises level 3
# 1. Go to the data folder and use the countrie.py file.
# Loop through the countries and extract all the countries containing the word 'land'
from countries import countries

for country in countries:
    if 'land' in country:
        print(country)

# 2. THis is a fruit list, reverse the order using loop
fruits = ['banana', 'orange', 'mango', 'lemon']
for fruits in reversed(fruits):
    print(fruits)
    
# 3. Go to the data folder and use the countries_data.py file
# i. What are the total number of languages in the data


from countries_data import countries_data

unique_language = set()

for country in countries_data:
    for language in country['languages']:
        unique_language.add(language)
print('Total number of languages: ', len(unique_language))

# ii. Find the ten most spoken language from the data

all_languages = [language for country in countries_data for language in country['languages']]

sorted_languages = sorted(set(all_languages), key=lambda x: all_languages.count(x), reverse=True)

top_ten_languages = sorted_languages[:10]
print('Top ten most used languages:')
for language in top_ten_languages:
    print(language)



# iii. Find the 10 most populator countries in the world
most_populated = sorted(countries_data, key=lambda x: x['population'], reverse=True)

top_ten_populated = most_populated[:10]
print('Top 10 most populated countries: ')
for country in top_ten_populated:
    print(f'{country['name']}: {country['population']}')