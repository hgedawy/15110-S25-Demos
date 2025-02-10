# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:02:23 2025

@author: hkg
"""

import random
import time
        
###################### USING PRINT
x = 42
print("The answer to the life, universe, and everything is", x, "!")


##### Mysterious

#  what is this code doing?
def mysterious(target, start, end): 
    if target < start or target > end:
        return None
    
    count = 0
    while True:
        print("count", count)
        x = random.randint(start, end) #need to import random
        print("x:", x)
        if x == target:
            return count + 1
        count += 1
   
print("mysterious----------")
print(mysterious(20, 2, 15))
print(mysterious(11, 3, 20))



######################  PRINT + SLEEP (need to import time)

def numberOfDigits(n): # BUGGY
    d = 0
    while n >= 0:
        print('n: ', n) 
        n = n // 10
        d = d + 1
    return d

print("numberOfDigits----------")
#print(numberOfDigits(168))



#FIXED CODE
def numberOfDigits_fixed(n):
    
    if n == 0:
        return 1
    
    d = 0
    n = abs(n)
    while n > 0:
        print('---------')
        print('n: ', n) 
        n = n // 10
        print('n %10 ', n%10) 
        d = d + 1
        print('d : ', d) 

    return d

print("numberOfDigits_Fixed----------")
print(numberOfDigits_fixed(168))
print(numberOfDigits_fixed(-168))
print(numberOfDigits_fixed(0))


######################  RANDOM MODULE TO CREATE TEST CASES
for i in range(20):
    x= random.randint(-100, 4000)
    print("============")
    print("x:", x)
    print(numberOfDigits_fixed(x))



######################  PRINT + ROUND
###round(number, ndigits) - 2nd arg is optional


### Example
def manyDigitsVSPrecision():
    v = 1
    for i in range (3, 50, 3):
        v = v + (v/2)
       # print("v:", v, v*v, v ** 3) 
        #print(round(0.5))
        print("v:", round(v,3), round(v*v, 2), round(v ** 3, 2)) 

    
print("manyDigitsVSPrecision----------")
print(manyDigitsVSPrecision())


######################  PRINT with STRING FORMATTING

### END argument: adds new line by default... can we change this?
print("Print with End Argument ----------")
print('Hello!')         
print('This is 15110.') 
print('A great course!')


print('Hello!', end='')         
print('This is 15110.', end='') 
print('A great course!')


print('Hello!', end=' ')         
print('This is 15110.', end=' ') 
print('A great course!')


print('Hello!', end=',')         
print('This is 15110.', end=',') 
print('A great course!')


### SEP (Seperator) argument: to remove unnecessary spaces *between printed items* or add any character?

print("print with SEP argument ----------")
x = 1
for i in range(1,10):
    x = x * i
    print(i,'!= ', x, sep=',')  # sep=''
    
print(10, 2, 2025, sep="-")

### Escapce Sequences

print("Print with Escapce Sequences ----------")
print(" 'Single Quotes' inside double ")
print(' "Double Quotes" inside Single')
     
### BUGGY 
print("He said, "What's there?" ") #SyntaxError: Invalid syntax
print('He said, "What's there?" ') # SyntaxError: Invalid syntax
      
###Fixed 
print("He said, \"What's there?\" ") #SyntaxError: Invalid syntax
print('He said, "What\'s there?" ') # SyntaxError: Invalid syntax



### Types of space chars   
print(" Hello!\nThis goes on a new line ")  
print(" Hello!\t\tThis gets two tab spaces ") 
#print("C:\Python64\Lib")# \\ : allows writing file/folder paths in windows
print(" This rings a bell\a") #this rings a bell!


### Example 
def mystery(n): 
    x = 0
    while(x != 1 and x != 4): 
        print('\n-------- Outer Loop ------', "x:", x)
        x = 0
        print('\t ----- Inner Loop ------',"n:", n)
        while (n != 0):
            x = x + (n % 10) ** 2
            n = n // 10
            print('\t\t', "n:", n, " x:", x)
        print('\t ----- Exited Inner Loop ------')
        n = x
    if x == 1:
        return True
    else:
        return False

print("Mystery ----------")    
print(mystery(42))


###################### Redirect Output to a File 
   
def checkValues(numbers):
    for v in numbers:
        print('Number:', v)
        if v % 3 == 0 and v % 2 == 0: 
                print('\tdivisible by 2 and 3')
        else:
            if v % 3 != 0:
                print('\tNot divisible by 3')
            if v % 2 != 0:
                print('\tNot divisible by 2')


print("checkValues ----------")    
#checkValues(range(1,100))

### w/ File
import sys #

def checkValuesWithFile(numbers):
    
    f = open("results.txt", 'w')
    sys.stdout = f
    
    for v in numbers:
        print('Number:', v)
        if v % 3 == 0 and v % 2 == 0: 
                print('\tdivisible by 2 and 3')
        else:
            if v % 3 != 0:
                print('\tNot divisible by 3')
            if v % 2 != 0:
                print('\tNot divisible by 2')
                
    f.close()

print("checkValuesWithFile ----------")    
checkValuesWithFile(range(1,100))   


###################### CONTROL STATEMENTS W/ LOOPS

#### BREAK: Terminates the loop prematurely (skip entire loop)
        
print("BREAK ----------")    
for i in range(5): 
    if i == 3:
        break #more common with while loops
    print(i)


## VS RETURN
def f(x):
    cnt = 1 
    while True: 
        xx = x ** cnt
        if xx > 100: 
            break   # return xx - 100
        print('Iteration', cnt, ' x:', xx )
        cnt += 1
    print('After Loop')
  
    return xx - 100 #remove

print("f() Break vs Return ----------")    

y = f(3)
print('y:', y)


#### continue: Skips the rest of the code inside the loop for the current iteration 
                #and proceeds to the next iteration.
                #rarely a good idea to use it
      
print("Continue ----------")    
for i in range(5):
    if i == 2:
        continue
    print(i)
    
def sumEvenNumbersSkip10():
    s = 0
    for num in range(1, 21):
        ### Edit to skip 10

        if num % 2 == 0:
            s += num
            print("Current Sum: ", s)
    return s

# print("sumEvenNumbersSkip10 ----------")    
#print(sumEvenNumbersSkip10())
