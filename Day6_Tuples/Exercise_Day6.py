# 1 Create an empty tuple
empty_tuple = tuple()
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and brothers
brothers = ("Lucken", "Lucky", "Edison", "Vincent")
sisters = ("Laura", "Joesline", "Camellia")

# 3. Join brothers and sister tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# 4. How many siblings do you have?
how_many = len(siblings)
print(how_many)

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
mom = ("Paulina")
dad = ("Letsmin")

siblings = list(siblings)
siblings.append(dad)
siblings.append(mom)
print(siblings)

family_members = tuple(siblings)
print(family_members)

# Exercise 2

# 1. Unpack siblings and parents from family_members
brother1, brother2, brother3, brother4, sister1, sister2, sister3, parent1, parent2 = family_members

# 2. Create fruits, vegetables and animal products tuples.
# Join the three tuples and assign it to a variable called food_stuff_tp
fruits = ("apple", "banana", "orange", "mango")
vegetables = ("spinach", "brocolli", "cucumber", "okra")
animal_products = ("leash", "cage", "dog_food", "cat_food")

food_stuff_tp = fruits + vegetables + animal_products

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from the tuple/list
length = len(food_stuff_lt)
middle_index = length // 2
if length % 2 == 0 :
    del food_stuff_lt[middle_index - 1:middle_index + 1]
else:
    del food_stuff_lt[middle_index]
    
print(food_stuff_lt)

# 5. Slice out the first three items and the last three items from food_staff_lt list
del food_stuff_lt[:3]
del food_stuff_lt[3:]
print(food_stuff_lt)

# 6. Delete the food_stuff_tp completely
# del food_stuff_lt
# del food_stuff_tp
# print(food_stuff_lt)
# print(food_stuff_tp)

"""7. Check if an item exists in tuple:
- Check if "Estonia" is a nordic country
- Check if "Iceland" is a nordic country
"""

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
