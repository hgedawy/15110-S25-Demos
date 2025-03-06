# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 12:33:44 2025

@author: hkg
"""

import math

############# ArmStrong Number #####################

### is_prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


### is_armstrong
def number_of_digits(n):
    count = 1
    digit = n
    while True:
        digit //= 10
        if digit == 0:
            return count
        else:
            count += 1


def get_kth_digit(n, k):
    n = abs(n)
    n = n // 10 ** k # keep only first k
    return n % 10 #return last one


def is_armstrong(n):
    n_digits = number_of_digits(n)
    power_sum = 0
    for k in range(n_digits):
        digit = get_kth_digit(n, k)
        power_sum += digit ** n_digits
    if power_sum == n:
        return True
    else:
        return False
    
    

### is_special_number
def is_special_number(n):
    prime, armstrong = False, False
    if is_prime(n):
        print(n, 'is prime!')
        prime = True
    
    if is_armstrong(n):
        print(n, 'is armstrong!')
        armstrong = True
    
    if prime or armstrong:
        return True
    else:
        return False
    
    
######################### Local VS Global Variables #######

print("\n Local VS GLobal #########################################")


### local scoping

def average(L):
    n_elements = len(L)
    avg = sum(L) / n_elements
    return avg

print("\n Local ########")

numbers = [1, 3, 6, 2]
x = average(numbers)
print(x)
#print(L)
#print(avg)
#print(n_elements)




### global scoping

def average_global():
    n_elements = len(L)
    avg = sum(L) / n_elements
    return avg

# L global
print("\n global ########")
L = [1, 3, 6, 2] 
x = average_global()
print(x)




### Clean way to define global scoping
def average_global():
    global L
    n_elements = len(L)
    avg = sum(L) / n_elements
    return avg

# L global
print("\n global ########")
L = [1, 3, 6, 2] 
x = average_global()
print(x)


###### Be Careful: when using global variables
x = 10

def f():
    global x
    y = x+1 # Reads x
    
    x= 3
    print("in f:", x)
    return y
  
f()
print("after f:", x)

### changes are propagated outside of the function!
def median():
   global L
   L.sort()
   return L[ len(L)//2 ]


L = [1, 3, 6, 2, 0]
m = median()
print(L)



######################### Named Parameters #######

def quadratic_roots(a, b, c):
    d = 1 / (2 * a)
    sqr = math.sqrt(b**2 - (4 * a *c)) 
    return (-b + sqr) * d, (-b - sqr) * d

print("\n Named Parameters #########################################")

# order matters
print(quadratic_roots(2, 5, 3))
print(quadratic_roots(3, 5, 2))


### how to do it in a way that would make it safe to change the order
#Passing arguments as keyword (named) arguments
print(quadratic_roots(a=2, b=5, c=3))
print(quadratic_roots(c=3, b=5, a=2))



### makes it more clear: SLIDES
# random_password(upper=1, lower=1, digits=1, length=8)
# random_password(1, 1, 1, 8)


# you saw an example before:
sorted(L, reverse=True) 


# Help(f): to know what the function takes as input and what it returns 
def f(a, b):
    """ f(a, b) takes two numbers as input 
    Returns the sum of a and b"""
    c = a + b
    return c

help(sum)
help(f)

######################### Default Parameters #######

def quadratic_roots_default(a = 1, b = -3, c = 2):
    d = 1 / (2 * a)
    sqr = math.sqrt(b**2 - (4 * a *c)) 
    return (-b + sqr) * d, (-b - sqr) * d
    
    
print("\n Default Parameters #########################################")

#A default value can be defined for each argument


#the parameter takes its default value, if no value passed
x1, x2 = quadratic_roots_default() # quadratic_roots_default(a = 1, b = -3, c = 2)
print("Default: ", x1, x2)

x1, x2 = quadratic_roots_default(b= 2, c= -3, a= 1) 
print("Default: ", x1, x2)

#if a value is passed for a parameter with a default value, the parameters takes the value of the provided argument


#### Equivelant Function Calls

print(quadratic_roots_default(b=2, c=-3) == quadratic_roots_default(a=1, b=2, c=-3)) #??
print(quadratic_roots_default(b=4) == quadratic_roots_default(a=1, b=4, c=2))



####################### Be careful mixing up positional and named parameters! 
print("\n XX Mixing Positional and Named Arguments XX #########################################")

x1, x2 = quadratic_roots_default(2, c=-3)
x3, x4= quadratic_roots_default(a=2, b=-3, c=-3)
print(x1==x3 and x2 == x4)

#issue 1
x1, x2 = quadratic_roots_default(2, a=-3)


#issue 2
#x3, x4= quadratic_roots_default(c=-3, 2, -3)
