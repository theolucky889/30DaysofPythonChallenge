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
