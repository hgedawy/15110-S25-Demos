# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 16:45:46 2025

@author: hkg
"""



################### isPalendromic

def isPalendromic(L):
    return L == L[::-1]
    
print("isPalendromic")
print(isPalendromic([1,2,3,2,1]))


################### Frequently Asked Questions

def faq(L, n):
    return []

# print(faq([10, 40, 20, 10, 40, 10], 2))  # Output: [10, 40]
# print(faq([1, 4, 2, 1, 3], 2))           # Output: [1]
# print(faq([1, 1, 3, 5, 4, 6, 3, 4], 3))  # Output: []


################### Detective Watson
def guilty(L):
    
    newL = sorted(L, reverse = True)
    val = newL[1]
    
    return L.index(val) + 1

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