# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 12:48:34 2025

@author: hkg
"""

def f1(s):
    return s[::2][::-1] + s[::-1][::2]

def f2(s):
    s = s[: len(s) // 2] + s[len(s) // 4 : len(s) - 1]
    return s

def ct1(magic):    
    print("1: ", f1(magic))
    print("2: ", f2(magic))
    return magic

print(ct1("112rocks"))



def nonVowelCount(s):
    """
    takes a string s and returns number of non-vowels inside s
    ignore case, A and a are both vowels
    """
    vowels= "aeiouAEIOU"
    
    counter=0
    for c in s:
        if  c not in vowels:
           counter+=1
        
    return counter

nonVowelCount("Hello")






################### FROM NOTES

def words(s):
    
    return []

# Test the function with the given example
test_string = "Once upon a time in a land far far away..."
print(words(test_string))



def mostFrequent(s):
    
    return ''

# Test the function with the given example
test_string = "exercise 2"
print(mostFrequent(test_string))


def combiner(s1, s2):
    return ''

# Test the function with the given example
s1 = "SaWr"
s2 = "tras"
print(combiner(s1, s2))  # Output should be "StarWars"


