# 1. Declare an empty list
empty_list = []
print(empty_list)

# 2. Declare a list with more than 5 items
list_five = ["apple", "strawberry", "melon", "lime", "mango"]

# 3. Find the length of your list
print(len(list_five))

# 4. Get the first item, the middle item and the last item of the list
first_middle_last = list_five[0:5:2]
print(first_middle_last)

# 5. Declare a list called mixed_data_types, put your name, age, height, martial status, address
mixed_data_types = ["Theodore", 22, 168, "single", "taipei"]

# 6. Declare a list variable named it_companies and assign initial values
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. print the list using print
print(mixed_data_types)
print(it_companies)

# 8. print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle, and last company
first_middle_last_company = it_companies[0:7:3]
print(first_middle_last_company)

# 10. Print the list after modifying one of the company
it_companies[3] = "Samsung"
last_company = len(it_companies) - 1
it_companies[last_company] = "SpaceX"
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("Viewsonic")
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(4, "BenQ")
print(it_companies)

# 13. Change one of the it_companies name to uppercase (IBM excluded)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# 14. Join the it_companies with a string "#"
print("#".join(it_companies))

# 15. Check if a certain company exists in the it_companies list
def check_company(company, it_companies):
    if company in it_companies:
        return True, it_companies.index(company)
    else:
        return False, None

user_input = input("Name a Company: ")
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# Stores the result
result = check_company(user_input, it_companies)
# Output
print(result)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
three_companies = it_companies[3:]
print(three_companies)

# 19. Slice out the last 3 companies from the list
last_three_companies = it_companies[0:4]
print(last_three_companies)

# 20. Slice out the middle IT company or Companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
no_middle = it_companies[0:3] + it_companies[4:]
print(no_middle)

# 21. Remove the first IT company from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
no_first = it_companies[1:7]
print(no_first)

# 22. Remove the middle IT company or companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
middle_index = len(it_companies) // 2  # This finds the middle index
del it_companies[middle_index]  # This deletes the middle element
print(it_companies)

# 23. Remove the last IT company from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop()
print(it_companies)

# 24. Remove all IT companies from the list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.clear()
print(it_companies)

# 26. Join the Following lists:
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "Mongodb"]
front_end.extend(back_end)
print(front_end)

# 27. After joining the list in #26. Copy the joined list and assign it to a variable full_stack then insert Python and SQL after Redux
full_stack = front_end + back_end
full_stack_copy = full_stack.copy()
full_stack_copy.insert(5, "Python")
full_stack_copy.insert(6, "SQL")
print(full_stack_copy)

# Exercise 2
"""
1. The following is a list of 10 student ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
- Sort the list and find the min and max age
- add the min age and the mage again to the list
- FInd the median age
- Find the average age
- Find the range of the ages (max minus min)
- Compare the value of (min - average) and (max - average), use abs() method
"""

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)     # 1

min_age = min(ages)
max_age = max(ages)
ages.append(min_age)
ages.append(max_age)
print(ages)     # 2

def median(ages):
    sorted_ages = sorted(ages)
    n = len(sorted_ages)
    
    if n % 2 == 1:
        return sorted_ages[n // 2]
    else:
        mid1 = sorted_ages[n // 2]
        mid2 = sorted_ages[n // 2]
        return (mid1 + mid2) / 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
median_age = median(ages)
print(median_age)       # 3

total_ages = sum(ages)
average_ages = total_ages / len(ages)
print(average_ages)     # 4

range_ages = max_age - min_age
print(range_ages)       # 5

min_average = min_age - average_ages
max_average = max_age - average_ages
abs_min_ages = abs(min_average)
abs_max_ages = abs(max_average)
print(abs_max_ages)
print(abs_min_ages)

# 2. Find the middle countries in the countries list
countries = ["USA", "Indonesia", "Taiwan", "China", "Malaysia", "Germany"]
countries.sort()

length_countries = len(countries)
if length_countries & 2 == 1:
    middle_country = countries[length_countries // 2]
    print(middle_country)
else:
    middle_country = countries[length_countries // 2 - 1 : length_countries // 2 + 1]
    print(middle_country)

# 3. Divide the countries list into two equal lists if it is even, if not, one more country for the first half
countries = ["USA", "Indonesia", "Taiwan", "China", "Malaysia", "Germany"]
countries.sort()

length_countries = len(countries)
mid_country = length_countries // 2 + length_countries % 2
first_half = countries[:mid_country]
second_half = countries[mid_country:]
print(first_half)
print(second_half)

# 4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# Unpack the first three countries and the rest as scandic countries
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
fight_countries = countries[0:3]
scandic_countries = countries[3:7]
print(fight_countries)
print(scandic_countries) 
