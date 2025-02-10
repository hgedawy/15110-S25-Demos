# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:02:37 2025

@author: hkg
"""

############### findFirstPrimeInRange ############

def findFirstPrimeInRange (start, end):
    return 42

print(findFirstPrimeInRange(10, 20))



############### DEBUG FIBONACCI ############
# Debug and fix this code
def fibonacci(n):
    f0 = 1
    f1 = 1
    
    for i in range(n):
        nextF = f0 + f1
        f0 = f1
        f1 = nextF
        
    return nextF

# assert(fibonacci(0) == 1)
# assert(fibonacci(1) == 1)
# assert(fibonacci(2) == 2)
# assert(fibonacci(3) == 3)
# assert(fibonacci(4) == 5)
# print("PASSED !!!")

############### printNumberTriangle ############
def printNumberTriangle(n):
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            print(j, end="")
        print()

printNumberTriangle(4)



############### rest23 ############
def rest23(x, y):
    return 42

#print(rest23(10, 25))




############### forbiddenZero ############
def forbiddenZero(n):
    while True:
        n += 1
        if '0' not in str(n):
            return n


#print(forbiddenZero(19))  # 21



############### triangle ############
def triangle(n):
    return None


#triangle(5)