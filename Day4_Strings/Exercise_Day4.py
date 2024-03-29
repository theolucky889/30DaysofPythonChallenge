# 1. Concantate the string "Thirty", "Days", "Of", "Python" to a single string, "Thirty Days Of Python"
days_python = ["Thirty", "Days", "Of", "Python"]
result = " ".join(days_python)
print(result)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
coding_all = ['Coding', 'For' , 'All']
result = " ".join(coding_all)
print(result)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
first_letter = company[0]

# 4. Print the variable company using print()
print(first_letter)

# 5. Print the length of the company string using len() method and print()
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
company_uppercase = company.upper()
print(company_uppercase)

# 7. Change all the characters to lowercase letters using lower() method.
company_lowercase = company.lower()
print(company_lowercase)

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company_capitalize = company.capitalize()
company_title = company.title()
company_swap = company.swapcase()

print(company_capitalize)
print(company_title)
print(company_swap)

# 9. Cut(slice) out the first word of Coding For All string.
first_word = company.split()[0]
print(first_word)

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))
substring = "Coding"
print(company.index(substring))
other_company = "Hello"
print(other_company.startswith("Coding"))
print(company.startswith("Coding"))

# 11. Replace the word Coding in the string "Coding for all" to Python
print(company.replace("Coding", "Python"))

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
for_all = "Python for Everyone"
print(for_all.replace("Everyone", "All"))
split_phrase = for_all.split()
split_phrase[-1] = "All"
new_phrase = " ".join(split_phrase)
print(new_phrase)

# 13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = companies.split(", ")
print(split_companies)

# 15. What is the character at index 0 in the string Coding For All.
index_zero = company[0]
print(index_zero)

# 16. What is the last index of the string Coding For All.
index_last = company[-1]
print(index_last)

# 17. What character is at index 10 in "Coding For All" string.
index_ten = company[10]
print(index_ten)

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
for_everyone = "Python For Everyone"
acronym = "".join(word[0] for word in for_everyone.split())
print(acronym)

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
for_all = "Coding For All"
new_acronym = "".join(word[0] for word in for_all.split())
print(new_acronym)

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
coding_sub = "C"
print(for_all.index(coding_sub))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
for_sub = "F"
print(for_all.index(for_sub))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(for_all.rfind("l"))

# 23. Use index or find to find the position of the first occurrence of the word 'because' 
# in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
you_cannot = "You cannot end a sentence with because because because is a conjunction"
bec_ause = "because"
print(you_cannot.index(bec_ause))

# 24. Use rindex to find the position of the last occurrence of the word because
# in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(you_cannot.rindex(bec_ause))

# 25. Slice out the phrase 'because because because' in the following
# sentence: 'You cannot end a sentence with because because because is a conjunction'
cannot_split = you_cannot.split()
slice_because1 = cannot_split[6]
slice_because2 = cannot_split[7]
slice_because3 = cannot_split[8]
print(slice_because1, slice_because2, slice_because3)

# 28. Does 'Coding For All' start with a substring Coding?
for_all = "Coding For All"
print(for_all.startswith("Coding"))

# 29. Does 'Coding For All' start with a substring coding?
for_all = "Coding For All"
print(for_all.startswith("coding"))

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
coding_spaces = '   Coding For All      '
trim_spaces = coding_spaces.strip()
print(trim_spaces)

"""
31. Which one of the following variables return True when we use the method isidentifier():
 - 30DaysOfPython
 - thirty_days_of_python
    """
python_1 = "30DaysOfPython"
python_2 = "thirty_days_of_python"

print(python_1.isidentifier(), python_2.isidentifier())

# 32. The following list contains the names of some of python 
# libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
# Join the list with a hash with space string.

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join_libraries = "# ".join(python_libraries)
print(join_libraries)

"""
33. Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.
"""
sentence = "I am enjoying this challenge. \nI just waonder what is next."
print(sentence)

"""
34. Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
"""
print("Name\tAge\tCountry\tCity")
print("Theodore\t21\tIndonesia\tJakarta")

"""
35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
"""
radius = 10
area = 3.14 * radius ** 2
formatting_sentence = "The area of a circle with radius %d is %.2f meters square."%(radius, area)
print(formatting_sentence)

"""
36. Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
    """
a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {}".format(a, b, a / b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))
print("{} % {} = {}".format(a, b, a % b))