# Program to add 2 different binary numbers

"""
Method : Convert the binary string to integer, then add them to get decimal sum, then
convert back to the binary format
"""

# Giving 2 binary input strings
x = input('Binary 1 : ')
y = input('Binary 2 : ')

# Converting binary numbers to integer equivalents
x = int(x, 2)
y = int(y, 2)

# Printing decimal equivalents
print('Decimal equivalent of x : ', x)
print('Decimal equivalent of y : ', y)

# Adding decimal equivalents and storing it in result
result = x + y

# Printing the decimal equivalent sum
print('Decimal sum : ', result)

# Converting result to binary format
# Note that binary format is of string type starting with '0b'
# It can be excluded by splitting the string ' [2:] '
result = bin(result)[2:]

# Printing the result in binary format
print('Binary sum : ', result)