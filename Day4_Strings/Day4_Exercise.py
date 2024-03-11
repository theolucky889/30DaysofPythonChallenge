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