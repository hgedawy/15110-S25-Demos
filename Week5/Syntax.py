# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:59:02 2025

@author: hkg
"""

########## For Loops RECAP

print("sequence of characters")
for c in "Hello":
    print(c)
    
print("sequence of items in a list")
for item in ["Hi", 12, True]:
    print(item)
    
print("sequence of numbers")
for i in 1,2,3,4,5:
    print(i)

# generating a sequence of numbers using range() function
print("range:")
for r in range(6): #0,1,2,3,4,5 # start =0 , step = 1
    print(r)

print("range with start = 1")
for s in range(1, 6): #1,2,3,4,5 # start = 1, step = 1
    print(s)
    
print("range with step = 2")
# I can reuse the loop variable name in another loop
for i in range(1, 6, 2): #1,3,5 # start=1, step = 2   
    print(i)    

### Sum of the first N numbers
def sum_first_for(n):
    s = 0
    for i in range(n+1):
        s = s + i
    return s

print("Sum of first 5 numbers using for: ", sum_first_for(5))




############### While Loops

# ### Sum of the first N numbers
def sum_first_while(n):
    i = 0
    s = 0
    while i <= n:
        s = s + i
        i = i + 1
    return s

print("Sum of first 5 numbers using while: ", sum_first_while(5))


##### Errors that we can face


### Infinite Loop
# i = 0
# s = 0
# while i <= 10:
#     s = s + i
#     i = i - 1
#     print("inside loop -- ", i)
# print("Exited While Loop")    



### Never Happening Loop
i = 0
s = 10
while s > 20:
    s = s + i
    i = i + 1
    print("inside loop -- ", i)
print("Exited While Loop")    


##### Interrupting the Loop

# BREAK: exits the loop
print("Interrupting loop")
i = 0
s = 0
while i <= 10:
    s = s + i
    if s >= 6:
        break
    i = i + 1
    print("inside loop -- ", i)
print("Exited While Loop s = ", s)    


# RETURN: Inside a function, return exits the loop (and the function!)
def f():
    print("Interrupting loop with return")
    i = 0
    s = 0
    while i <= 10:
        s = s + i
        if s >= 6:
            return s, i
        i = i + 1
        print("inside loop -- ", i)
    print("Exited While Loop s = ", s) 

f()
print("outside the function")