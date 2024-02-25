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
