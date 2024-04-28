# Exercise Level 1
# 1. Write a function which generates a six digit/character random_user_id
from random import choices
import string

def random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(choices(characters, k = 6))

print(random_user_id())
'1ee33d'

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn't take any
# parameters but it takes two inputs using input(). One of the inputs is the number of 
# characters and the second input is the number of IDs which are supposed to be generated

def user_id_gen_by_user():
    num_chars = int(input('Enter the number of characters for User ID: '))
    num_id = int(input('Enter the number of ID to generate: '))

    id = []
    characters = string.ascii_letters + string.digits
    for _ in range(num_id):
        id.append(''.join(choices(characters, k = num_chars)))
    
    return id

for user_id in user_id_gen_by_user():
    print(user_id)
    
# 3. Write a function named rgb_color_gen. It will generate rgb colors(3 values ranging from 0 to 255)
from random import randint

def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb_val = f'rgb({r},{g},{b})'
    return rgb_val

print(rgb_color_gen())
# rgb(125, 244, 255)

# Exercise Level 2
'''
1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
(six decimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9
and first 6 letters of the alphabet, a-f. Check the task 6 for output examples)
2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array
3. Write a function generate_colors which can generate any number of hexa or rgb colors
'''

def list_of_hexa_colors(n):
    hex_chars = '0123456789abcdef'
    return ['#' + ''.join(choices(hex_chars, k=6))for _ in range(n)]

def list_of_rgb_colors(n):
    return [f'rgb({randint(0, 255)},{randint(0, 255)},{randint(0, 255)})' for _ in range(n)]

def generate_colors(color_type, n):
    if color_type == 'hex':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return ['Invalid Input']

print(generate_colors('hex', 3))  # Outputs something like ['#a3e12f', '#03ed55', '#eb3d2b']
print(generate_colors('hex', 1))  # Outputs something like ['#b334ef']
print(generate_colors('rgb', 3))   # Outputs something like ['rgb(5, 55, 175)', 'rgb(50, 105, 100)', 'rgb(15, 26, 80)']
print(generate_colors('rgb', 1))   # Outputs something like ['rgb(33, 79, 176)']

# Exercise Level 3
'''
1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
2. Write a function which returns an array of seven random numbers in range of 0-9. All the numbers should be unique
'''
from random import sample

def shuffle_list():
    return sample(range(10), 7)

print(shuffle_list())