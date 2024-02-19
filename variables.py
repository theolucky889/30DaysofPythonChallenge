#Exercise - Day 2
first_name = 'Theodore Lucky'
last_name = 'Tendy'    
full_name = 'Theodore Lucky Tendy'
country = 'Indonesia'
city = 'Jakarta'
age = 22
year = 2002
is_married = False
is_true = False
is_light_on = True

first_name, last_name, full_name, age, year, country = 'Joesline', 'Suryadi', 'Joesline Suryadi', 25, 1999, 'Tangerang'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print('Your first name has:', len(first_name),'letters.', 'while your last name has:', len(last_name), 'letters.')

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

varTotal = num_one + num_two
varDiff = num_two - num_one
varProduct = num_two * num_one
varDivision = num_one / num_two
varRemainder = num_two % num_one
varExp = num_one ** num_two
floor_division = num_one // num_two

print(varTotal)
print(varDiff)
print(varProduct)
print(varDivision)
print(varRemainder)
print(varExp)
print(floor_division)

r_Circle = 30
pi = 3.14
area_of_circle = pi*r_Circle*r_Circle
circum_of_circle = 2*pi*r_Circle

#Get input from user to claculate the area of circle
radius = int(input('radius of circle: '))
pi = 3.14
area_of_circle_input = pi*radius*radius
print(area_of_circle_input)

#Get input from user for personal data
first_name = input('First Name: ')
last_name = input('Last Name: ')
country = input('Country: ')
age = int(input('Age: '))

print('Hello, ', first_name, last_name, 'you are from ', country, 'and you are ', age, 'years old')




