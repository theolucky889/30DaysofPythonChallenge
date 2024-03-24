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

