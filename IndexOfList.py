# Program to return indices of a (repetitive) value in an arranged list

"""
Method : sort the list, use for loop and store the index where the value repeats
"""

# Giving an input number list and a value whose indices are to be found
In_list = [int(i) for i in input('Enter a list : ').split()]
value = int(input('Enter a value : '))

# Calculating the length of the list
ListLength = len(In_list)

# Before sorting
# Creating an empty list to store the indices before sorting
Index_list1 = []

# Looping through the list to find where the value is found
for index in range(ListLength):
    if In_list[index] == value:
        Index_list1.append(index)

# Printing the resultant list with the indices
print('The index list before sorting is : ', Index_list1)

# Sorting the list
# Arranging (Sorting) the list in increasing order
In_list = sorted(In_list)

# Printing the sorted list
print('The sorted list is : ', In_list)


# Creating an empty list to store the indices after sorting
Index_list2 = []

# Looping through the list to find where the value is found
for index in range(ListLength):
    if In_list[index] == value:
        Index_list2.append(index)

# Printing the resultant list with the indices
print('The index list after sorting is : ', Index_list2)