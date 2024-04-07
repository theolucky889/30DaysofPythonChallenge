# 1. Iterate 0 to 10 using for loop, do the same thing using while loop
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     print(number)

for number in range(11):
    print(number)

number = 0
while number < 11:
    print(number)
    number = number + 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop
for number in range (10, -1, -1):
    print(number)

number = 10
while number >= 0:
    print(number)
    number = number - 1

# 3. Write a loop that makes seven calls to print(), so we get on the output of the following triangle:
"""
#
##
###
####
#####
######
#######
"""
hashtag = '#'
for i in range(7):
    print(hashtag)
    hashtag += '#' 

# 4. Use nested loops to create the following:
"""
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""
hashtag = '#'
for row in range(8):
    row_str = ''
    for col in range(8):
        row_str += hashtag + ' '
    print(row_str)
    
# 5. Print the following pattern:
"""
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""
