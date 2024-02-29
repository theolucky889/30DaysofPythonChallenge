# Create a string
letter = 'p'                # A string could be a single character or a bunch of texts\
print(letter)               # p
print(len(letter))          # 1
greeting = 'Hello World!'   # String could be made using a single or double quote, "Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

# Multiline string is created by using single(''') or triple double quotes("""")
multiline_string = '''I am a student and enjoy learning.
I didn't find anything as rewarding as learning new things.
That is why I am learning python again.'''
print(multiline_string)

# Another way of doing the same thing is by using (""")

# String Concatenation
# We can connect strings together. Merging or connecting strings is called concatenation.
first_name = "Theodore Lucky"
last_name = "Tendy"
space = " "
full_name = first_name + space + last_name
print(full_name)    # Theodore Lucky Tendy
# Checking the length of a string using len() built-in function
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))
