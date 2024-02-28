"""Variables
    Variables store data in a computer memory. Mnemonic variables are recommended to 
    use in many programming languages. A mnemonic variable is a variable name that can 
    be easily remembered and associated. A variable refers to a memory address in which 
    data is stored. Number at the beginning, special character, hyphen are not allowed
    when naming a variable. A variable can have short name (like x, y, z), but a more
    descriptive name (firstname, lastname, age, country) is highly recommended
    """
    
"""Python Variable Name Rules
    - A varibale name must start with a letter or the underscore character
    - A variable name cannot start with a number
    - A varibale name can only contain alpha-numeric characters and underscores (A-z, 0-9. and _)
    - Variable names are case-sensitive ((firstname, Firstname, FirstName and FIRSTNAME) are different variables)
    """
    
"""#Examples
    firstname
    lastname
    age
    country
    city
    first_name
    last_name
    capital_city
    _if # if we want to use reserved word as a variable
    year_2021
    year2021
    current_year_2021
    birth_year
    num1
    num2
    """ 
    
"""#Invalid Variable Names
    first-name
    first@name
    first$name
    num-1
    1num
    """
    
"""
    Python developers have adopted a variable naming style which is called snake case(snake_case)
    EX: first_name, last_name, engine_rotation_speed
    """
    
    #example
    #Variables in Python
first_name = 'Theodore Lucky'
last_name = 'Tendy'
country = 'Indonesia'
city = 'Jakarta'
age = 22
is_married = False
skills = ['HTML', 'CSS', 'JS', 'Python', 'React']
person_info = {
    'firstname':'Theodore Lucky',
    'lastname':'Tendy',
    'country':'Indonesia',
    'city':'Jakarta'
}

#using print() and len() built-in functions on variables
print('Hello, Wporld!') #The text Hello, World! is an argument
print('Hello',',', 'World','!') #It can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) #It takes only one argument

#Printing the values stored in the variables
print('FIrst name: ', first_name)
print('First name length: ', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', (last_name))
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

#Declaring Multiple Variable in a Line
#Multiple variables can also be declared in one line:
first_name, last_name, country, age, is_married = 'Theodore Lucky', 'Tendy', 'Jakarta', 22, False

print(first_name, last_name, country, age, is_married)
print('First name: ', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#Getting user input using the input() function.
first_name = input('What is your name: ')
age = input('How old are you?: ')

print(first_name)
print(age)

#Data Types
#To identify the data type we use the 'type' built-in function.

#Checking data types and casting
first_name = 'Theodore Lucky'   #str
last_name = 'Tendy'             #str
country = 'Indonesia'           #str
city = 'Jakarta'                #str
age = 22                        #int

#printing out data types
print(type('Theodore Lucky'))                                   #str
print(type(first_name))                                         #str
print(type(10))                                                 #int
print(type(3.14))                                               #float
print(type(1 + 1j))                                             #complex
print(type(True))                                               #bool
print(type([1, 2, 3, 4]))                                       #list
print(type({'name', 'Theodore', 'age', 'is_married'}))          #dict
print(type((1,2)))                                              #tuple
print(type(zip([1,2],[3,4])))                                   #set

"""Definition
Casting = Converting one data type to another data type, we use int(), float(), str(),
          list, set When we do arithmetic operations string numbers should be first converted
          to int or float otherwise it will return an error. If we concatenate a number with
          a string, the number should be first converted to a string.
"""
#Casting Example

#int to float
num_int = 10
print('num_int', num_int)               #10
num_float = float(num_int)
print('num_float: ', num_float)         #10.0

#float to int
gravity = 9.81
print(int(gravity))                     #9

#int to str
num_int = 10
print(num_int)                          #10
num_str = str(num_int)
print(num_str)                          #'10'

#str to int or float
num_str = '10.6'
print('num_int', int(num_int))          #10
print('num_float', float(num_str))      #10.6

#str to list
first_name = 'Theodore'
print(first_name)                       #Theodore
first_name_to_list = list(first_name)
print(first_name_to_list)               #['T', 'h', 'e', 'o', 'd', 'o', 'r', 'e']

