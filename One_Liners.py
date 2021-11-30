# ************** 1. Type-casting string to integer **************

str1 = '0'
str2 = '35'
print(int(str1), int(str2))
# Converts String 0 and 35 to int 0 and 35


# ************** 2. Reversing a list **************

arr = [1, 2, 3, 4, 5, 6, 7]
reversedArr = arr[::-1]
# Index representation, an alternate to using looping statements
print(reversedArr)

# ************** 3. Using in-built reversed() Function **************

arr1 = [1, 2, 3, 4, 5, 6, 7]
reversedArr1 = rlist(reversed(arr1))

# It is an alternative to index representation, with a reversed function which takes an array as an argument


# ************** 4. Using in-built reversed Method **************

arr2 = [1, 2, 3, 4, 5, 6, 7]
arr2.reverse()  # In-built method, a function that calls itself when called, similar to a.sort() and a.pop()

# ************** 5. Swap Two variables **************

variable1 = 25
variable2 = 35
variable1, variable2 = variable2, variable1

''' 
This declaration directly swaps the values of var1 and var2 instead of using three lines using 
a temporary variable as 
temp = var2
var2 = var1
var1 = temp
'''

# ************** 6. Check if a String is a palindrome or not **************

string1 = "MOM"
string2 = "MADAM"
string3 = "python"
string4 = "1234321"
print('Yes') if string1 == string1[::-1] else print('No')
print('Yes') if string2 == string2[::-1] else print('No')
print('Yes') if string3 == string3[::-1] else print('No')
print('Yes') if string4 == string4[::-1] else print('No')

# ************** 7. Find factorial of a number **************

# The factorial of a non-negative integer n can be found out by using lambda functions

number = 5
factorial = lambda number: 1 if number <= 1 else number * factorial(number - 1)
print("factorial of ", number, ": ", factorial(number))

# ************** 8. Calculate the sum of a list **************

# THe sum of values inside a list can be calculated using in-built function sum()

list1 = [1, 2, 3, 4, 5, 5, 7, 7, 7, 6, 6]
print(sum(list1))
