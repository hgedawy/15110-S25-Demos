# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 16:45:46 2025

@author: hkg
"""

################### Destructive and Non-Destructive RemoveEvens

def nondestructiveRemoveEvens(L):
	return []

def destructiveRemoveEvens(L):
    return None #No Return
            



L = [54, 21, 42, 76, 33]
assert(nondestructiveRemoveEvens(L) == [21, 33])

destructiveRemoveEvens(L)
assert(L == [21, 33]) #no returned value -L itself is changed



################### Frequently Asked Questions

def faq(L, n):
    return []

print(faq([10, 40, 20, 10, 40, 10], 2))  # Output: [10, 40]
print(faq([1, 4, 2, 1, 3], 2))           # Output: [1]
print(faq([1, 1, 3, 5, 4, 6, 3, 4], 3))  # Output: []


################### Detective Watson
def guilty(L):
    return 42

print(guilty([3, 5, 2]))           # Output: 1
print(guilty([1, 15, 3, 5, 2]))    # Output: 4


################### Corridor
def mana(L):
    return 42

print(mana([-2, 5, -1, 8, -11, 7, 3]))  # Output: 12
print(mana([-1, 2, -3]))               # Output: 2


################### Door Lock
def doorUnlock(L, h):
    return 42

print(doorUnlock([45, 45, 55, 55], 50))  # Output: 10
print(doorUnlock([84, 39, 17, 72, 94], 84))  # Output: 77