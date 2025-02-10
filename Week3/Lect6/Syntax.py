# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:02:04 2025

@author: hkg
"""

##### Boolean Types
x = True
print(x)

#### Boolean Expressions: expression that evaluates to True or False
print((2+3)>5)

#### Comparison (Relational) Operators 

#equality ==
a = 1
b = 5
c = (a==b)
print(c)
print(2.5 == 3.0)
print(2 == 2.0)


#disequality(not equal) !=
x = 4
y = 4.0
print(x!=y)


#less than <
print(a < b)

#less than or equal <= 
print(x <= y)

#greater than >
print(a > b)

#greater than or equal >=
print(a >= b)


#### multiple comparison operators in one expression- BE CAREFUL
print(a < x < b) # Python interprets this as a<x and x<b

print((a<x) <b) #evaluates (a<x) first which gives True.. then Python interprets True as 1 so it checks if 1 < b.
print(True == 1)
print(True+1) # interprets True as 1

print(1>0<1)
print((1>0) < 1)# 1< 1? False



#### Boolean (Logical) Operators 

## e1 AND e2: evaluates to True if e1 and e2 both evaluate to True
print(True and False)
print((2 != 3) and (4.5 > 4))
print( (2 != 2) and (8 == 8)) 
print( (2 != 3) and (True == False)) 
print ( (2 != 2) and (3 >= 1.5)) 

in_range = (x >= 0) and (x <=5)
print(in_range)


## e1 OR e2: evaluates to True if either e1 or e2 evaluate to True
print(True or False)
print((2 == 3) or (4.5 < 4)) #
print( (2 != 2) or (8 == 8)) 
print( (2 != 3) or (True == False)) 
print ( (2 != 2) or (3 <= 1.5)) #


x = x % 5
y =(x == 2) or (x == 3)
print(x, y)

print((x == 5) or (x == 6) or (x == 7))


## NOT e: evaluate to True if e evaluates to False
print(not (4.5 < 4) )
print(not (8 != 7))
print(not (False) )
print(not 0 < 4)


#### Precedence Rules: Arithmatic (b-e-dm-as), then relational, then logical
print(x*5 >= 10 and y-6 > 20)


#### Flow Control w/ Conditional Excution

#if-else
def conditionalFunction(x):
    if x >= 0:
        return "positive!"
          # ... other commands may appear here, for example, another assignment or another if!
    else:
        return "negative." # else case cannot be empty
    
print(conditionalFunction(20))
print(conditionalFunction(-5))


#if without else
def conditionalFunction_NoElse(x):
    if x >= 0:
        return "positive!"
          # ... other commands may appear here, for example, another assignment or another if!
    return "negative." # else case cannot be empty

print(conditionalFunction_NoElse(20))
print(conditionalFunction_NoElse(-5))


#if-elif
def sign(n):
    s = 0
    if n < 0:
        s = -1
    elif n > 0:
            s = 1
    #else:
    #    s = 0
        
    return s
        
sign(-43)

#nested
def nestedConditional(x,y):
    # A bad way of doing conditionals...
    if x >= 0 :
        if y >= 0:
            print("Both numbers are Positive")
        else:
            print("x is positive, y is negative")
    else:
        if (y >= 0):
            print("y is positive, x is negative")
        else:
            print("Both numbers are negative")

print("First call")
nestedConditional(10,20)
print("Second call")
nestedConditional(-5,-10)
print("Third call")
nestedConditional(20,-10)
print("Fourth call")
nestedConditional(-5,100)

# A better function
def betterFunction(x,y):
    if x >= 0 and y >= 0:
        print("Both numbers are Positive")
    elif x >= 0 and y < 0: 
        print("x is positive, y is negative")
    elif x < 0 and y >= 0:
        print("y is positive, x is negative")
    else:
        print("Both numbers are negative")

