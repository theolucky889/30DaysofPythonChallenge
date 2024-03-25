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

# 2. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)