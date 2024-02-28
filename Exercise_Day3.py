# Declare your age as integer variable
age = 22

# Declare your height as a float variable
height = 167.5

# Declare a variable that store a complex number
idk = 1 + 1j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle
base_triangle = float(input("Enter base of triangle: "))
height_triangle = float(input("Enter height of triangle: "))
area_of_triangle = 0.5 * base_triangle * height_triangle
print("The area of the triangle is: ", area_of_triangle)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle
# Calculate the perimeter of the triangle (perimeter = a + b + c)
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter_of_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is: ", perimeter_of_triangle)

# Get the length and width of a rectangle using prompt. Calculate its area and perimeter
length_rectangle = int(input("Enter length of rectangle: "))
width_rectangle = int(input("Enter width of rectangle: "))
area_of_rectangle = length_rectangle * width_rectangle
perimeter_of_rectangle = 2 * (length_rectangle * width_rectangle)
print("The area of the rectangle is: ", area_of_rectangle)
print("The perimeter of the rectangle is: ", perimeter_of_rectangle)

# Get radius of a circle using prompt. Calculate the area and circumference. pi = 3.14
radius_circle = float(input("Enter the radius of circle: "))
pi = 3.14
area_of_circle = pi * radius_circle * radius_circle
circumference__circle = 2 * pi * radius_circle
print("The area of the circle is: ", area_of_circle)
print("The circumference of the circle is: ", circumference__circle)

# Calculate the slope, x-intercept and y-intercept of y = 2x - 2
# Equation: y = 2x - 2
slope_1 = 2
y_intercept = -2

# X-interecept, y = 0
x_intercept = -y_intercept / slope_1

print("Slope= ", slope_1)
print("X-intercept= ", x_intercept)
print("Y-intercept= ", y_intercept)

# Slope is (m = y2-y1/x2-x1). Find the slope and euclidean distance between point(2,2) and point(6,10)
# Coordinates of the point
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calculate the slope
slope_2 = y2-y1/x2-x1

# Calculate Euclidean distance
euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print("Slope= ", slope_2)
print("Euclidean Distance= ", euclidean_distance)

# Compare the result of the slopes
# Slope from equation y = 2x - 2
slope_equation = 2

# Slope between points (2,2) and (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2-y1) / (x2-x1)

# Compare the slopes
if slope_equation == slope_points:
    print("The slopes are equal")
    print("Slope from equation y = 2x - 2: ", slope_equation)
    print("Slope between points (2,2) and (6,10): ", slope_points)
else:
    print("The slopes are not equal")
    print("Slope from equation y = 2x - 2: ", slope_equation)
    print("Slope between points (2,2) and (6,10): ", slope_points)
    
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# define the coefficients of the quadratic equation
a = 1
b = 6
c = 9

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check if the discriminant is non-negative
if discriminant >= 0:
    # Calculate the square root of the discriminant
    sqrt_discriminant = discriminant ** 0.5
    
    # Calculate the two possible solutions for x
    x1 = (-b + sqrt_discriminant) / (2*a)
    x2 = (-b - sqrt_discriminant) / (2*a)
    
    # Print the solution
    print("Solution 1: x = ", x1)
    print("Solution 2: x = ", x2)
else:
    print("No real solution exist")

# Comparison statement
pyth_len = "python"
drag_len = "dragon"
print(len(pyth_len) != len(drag_len))   # Falsy comparison statement

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on in python", "on" in "python")
print("on in dragon", "on" in "dragon")

# I hope this course is not full of jargon. Use in operator tocheck if jargon is in the sentence
sentence = "I hope this course is not full of jargon."
print("Is jargon in the sentence?", "jargon" in sentence)

# There is no 'on' in both dragon and python
print("on is not in dragon", "on" not in "dragon")
print("on is not in python", "on" not in "python")

# Find the length of the text python and convert the value to float and convert it to string
python_text = "python"
len_size = len(python_text)
print(len_size)

float_len_size = print(float(len_size))     # Convert to float
str_len_size = print(str(len_size))         # Conver to string

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python
# Function to check if a number is even
def is_even(number):
    return number % 2 == 0
"""
# Test the function
number = 6
if is_even(number):
    print(number, "is even")
else:
    print(number, "is odd")
    """
number = float(input("Enter number: "))
if is_even(number):
    print(number, "is even")
else:
    print(number, "is odd")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
# Floor division of 7 by 3
floor_division_result = 7 // 3

# Conver 2.7 to an integer
int_convert_value = int(2.7)

# Check if they are equal
if floor_division_result == int_convert_value:
    print("The floor division of 7 by 3 is equal to the integer converted value of 2.7")
else:
    print("The floor division of 7 by 3 is not equal to the integer converted value of 2.7")

# Check if type of '10' is equal to type of 10
if type('10') == type(10):
    print("type '10' is equal to the type of 10")
else:
    print("type of '10' is not equal to the type of 10")
    
# check if type of '9.8' is equal to type of 10
if type(9.8) == type(10):
    print("type of '9.8' is equal to type of 10")
else:
    (print("type of '9.8' is not equal to type of 10"))
    
# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person
hours_worked = float(input("Enter Hours Worked = "))
rate_per_hour = float(input("Rate per hour = "))
weekly_earning = hours_worked * rate_per_hour
print("Your weekly earning is: ", weekly_earning)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years_lived = float(input("Enter number of years you have lived: "))
years_to_seconds = 365 * 24 * 60 * 60
print("You have lived for: ", years_to_seconds, "seconds")

# Write a Python script that displays the following table
"""
1 1 1 1 1 
2 1 2 4 8 
3 1 3 9 27 
4 1 4 16 64 
5 1 5 25 125 
"""

# Define the number of rows and columns
num_rows = 5
num_columns = 5

# Generate the table
for i in range (1, num_rows + 1):
    # Print the first column (i)
    print(i, end='')
    
    #Print the subsequent columns
    for j in range(1, num_columns):
        # Calculate the value for each column(i^j)
        value = i ** j
        print(value, end='')
    # Move to the next row
    print()
