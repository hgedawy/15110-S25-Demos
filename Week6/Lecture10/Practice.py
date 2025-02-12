# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:17:54 2025

@author: hkg
"""


############# remove_duplicates
def remove_duplicates(lst):
    result = []
    for element in lst:
        if element not in result:
            result.append(element)
    return result

my_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(my_list))  


#############merge_alternately
def merge_alternately(L1, L2):
    return []

# Example usage
list1 = [1, 3, 5]
list2 = [2, 4, 6, 8]
# print(merge_alternately(list1, list2)) 




#############times10

def times10(L):
    return []

# print(times10([1, 2, 3]))  


#############maxValue
def maxValue(L):
    return 42

# print(maxValue([1, 2, 3, 4, 5]))  


#############binToDec
def binToDec(B):
    return 42

# print(binToDec([1, 1, 0]))  


#############count
def count(L, e):
    return 42

# print(count([1, 2, 2, 3, 2], 2))  


#############allTheSame
def allTheSame(L):
    return False

# print(allTheSame([1, 1, 1]))  
# print(allTheSame([1, 2, 1])) 










