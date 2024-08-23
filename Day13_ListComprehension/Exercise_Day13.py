# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero_numbers = [i for i in numbers if i <= 0]
print(negative_zero_numbers)

# 2. Flatten the following list of lists of lists to a one dimensional list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat1 = [number for row in list_of_lists for number in row]
flattened_list = [number for row in flat1 for number in row]
print(flattened_list)

"""output
[1, 2, 3, 4, 5, 6, 7, 8, 9]"""

# 3. Using list comprehension create the following list of tuples:
""" Output should look like this:
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
"""
# [(n, 1, n**1, n**2, n**3, n**3, n**4, n**5)]

result = [(n, 1, n**1, n**2, n**3, n**3, n**4, n**5) for n in range(11)]
print(result)


# 4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
"""output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]"""

flattened_countries = [[country.upper(), country[:3].upper(), capital.upper()]
                       for country_list in countries
                       for country, capital in country_list]
print(flattened_countries)

# 5. Change the following list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
"""output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]"""

dictionary_countries = [{'country': country.upper(), 'city': capital.upper()}
                        for country_list in countries
                        for country, capital in country_list]
print(dictionary_countries)

# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
"""output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']"""

concat_strings = [[name for row in names for name in row]
                  for name_list in names
                  for names in name_list]
print(concat_strings)