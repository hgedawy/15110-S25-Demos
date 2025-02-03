# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:59:15 2025

@author: hkg
"""
################## Act Like a computer

def f1(b, c):
    a = 0  
    while b > c: 
        b = b - c  
        a = a + 1  
    return a  

print(f1(25, 7)) 


def f2(b, c):
    a = 0  
    while b > c:
        b = b - c
        a = a + 1
        if (a + b)%2 == 1:
            break
    print(a+b)
    return a  

print(f2(25, 7))


################## Divide Until Fractional
def divideUntilBelowOne(x):
    count = 0
    while x > 1:
        x /= 2
        count += 1
    return count

# Example usage:
print(divideUntilBelowOne(100))  # Output: 7



################## Number of Digits
def numberOfDigits(n):
    d = 0
    while n > 0:
        n = n // 10;
        d = d + 1
        
    return d

print(numberOfDigits(123456789))



################## Nearest Factorial
def nearestFactorial(n):
    # Initialize variables
    factorial = 1
    i = 1
    
    # Calculate factorial values until it exceeds n
    while factorial * i <= n:
        factorial *= i
        i += 1
    
    # Return the integer whose factorial is the nearest to n while not being greater than n
    return i - 1

# Test the function with the given example
print(nearestFactorial(25))  # Output should be 4



################## Population Increase

def populationIncrease(pa, pb, ga, gb):
    days = 0
    while pa <= pb:
        pa += int(pa * ga / 100)
        pb += int(pb * gb / 100)
        days += 1
    return days 

assert(populationIncrease(100, 150, 1.0, 0) == 51)
assert(populationIncrease(90000, 120000, 5.5, 3.5) == 16)
assert(populationIncrease(56700, 72000, 5.2, 3.0) == 12)
assert(populationIncrease(123, 2000, 3.0, 2.0) == 300)
assert(populationIncrease(100000, 110000, 1.5, 0.5) == 10)
assert(populationIncrease(62422, 484317, 3.1, 1.0) == 100)


################## Straggler 


def straggler(fast, slow):
    return 42

#print(straggler(5, 7))  # Output should be 4