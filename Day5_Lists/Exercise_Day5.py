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