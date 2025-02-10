# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 09:23:48 2025

@author: hkg

"""
import math

### Kind of Object

# literal
print(42)
print("Hello")

# variable
x = 42
print(x)

greeting = "Hello"
print(greeting)



### Object types

# Numeric - scalar
a = 2 #integer
print(a)

#z= 02

b = 2.5 # floating points
print(b)


# Logical (binary) - scalar
t = True
f = False


# Character String - nonscalar
s1 = 'Hello'
s2 = "15110"
print(s1, s2)
print(s1[2])


# Structured ways to represent groups - nonscalar
l1 = [1, 2, 3]
l2 = [150, "Hello", True]
print(l1)
print(l2)

l1[1] = 100
print(l1)

### knowing object type
print(type(a))
print(type(t))
print(type(s1))
print(type(s2))
print(type(l1))



### Operators for numeric types

#addition
print(a+b)

#subtraction
print(a-b)


#multiplication
print(a*b)

#power
print(a**b)

c = 5

#division
print(c/a)

#integer division
print(c//a)

#mod
print(c%a)



### precedence in arithmatic operators
a = 6+3*4-6/3
print(a)

c = 5 - 4 - 3
d = (5-4)-3
e = 5 - (4-3)
print(c,d,e)

f = 2 ** 3 **4
g = (2**3) **4
h = 2**(3**4)
print(f,g,h)

### Useful functions in arithmatic

#abs
print(abs(-2))
print(abs(2))

#floor: rounds down
print(math.floor(1.5))
print(math.floor(-1.5))
print(math.floor(1.999))


#ceil: rounds up
print(math.ceil(1.5))
print(math.ceil(-1.5))
print(math.ceil(1.999))


#max
mx = max(1, 4, 100)
print(mx)

#min
mn = min(-2, 10, 5)
print(mn)