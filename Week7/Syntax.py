# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 16:02:52 2025

@author: hkg
"""

################### Documentation
#https://docs.python.org/3/library/stdtypes.html#list and
#https://docs.python.org/3/tutorial/datastructures.html#more-on-lists.



################### Parallel assignment
print("--------------- Parallel assignment --------------- ")

T = (4,3,2,1) 
# a = T[0] 
# b = T[1] 
# c = T[2] 
# d = T[3] 

# parallel assignment 

a, b, c, d = T
print("a =", a) 
print("b =", b) 
print("c =", c) 
print("d =", d) 


def f(x):
    return x*2, x*3
print(f(10))

#parallel assignment
x1, x2 = f(10)
print(x1, x2)



#Number of values on the right should equal the number of variables on the left
L = [1,2,3] 
# y, z = L
#y, z, i, e = L


############# Lists/Tuples Comparisons
print("--------------- Lists Comparisons --------------- ")

L1 = [0, 1, 5, -5]
L2 = [1, 3, 6, 0]
L3 = [0, 1, 4, 7]
L4 = [1, 3, 6, 0, 9]

print(L1 > L2)
print(L1 == L3)
print(L2 == L4)
print(L1 > L3)
print(L2 > L3)



############# max/min
#min(L) : Returns the item with the minimum value 
#max(L) : Returns the item with the maximum value 

print("---------------  max/min --------------- ")
print(min(L))
print(max(L))



############ sum
    #sum(L) : Returns the  sum of the elements in the list/tuple L

print("--------------- sum-------------- ")
print(sum(L))


#???????????? How to find the Avg
print(sum(L)/len(L))



#################### Finding An Element 

#### finding item by index
print("--------------- Finding An Element  --------------- ")
L = [ [11,12,13], [21,22,23], [31,32,33] ]
# last_list = L[-1]
# x = last_list[0]
x = L[-1][0]
print("x =", x)


#### finding item by value(content)
##L.index(item) Returns the index of the first occurrence of item in the list/tuple L

scores = [1, 11, 5, 11, 4, 11, 7, 9, 0, 4]
print(scores.index(11))
#print(scores.index(3)) #Error

#L.index(item, start) 
ns = scores.index(11, 4)  #L STARTING from start
print(ns)


############## Counting
    #count(item) : Returns the number of occurrences of item in the list/tuple L

print("--------------- Counting --------------- ")
n= scores.count(11)
print(n)



################### Destructive vs Non-Destructive operations

# A good way to rememebr is that 
#l.f() are usualky destructive ...  
#f(l) are not destructive, original doesn't change and a new copy is created


########### Adding List Elements
### L1+L2 (concatenates the two lists): creates a new list
    #+[e] is NONE DESTRUCTIVE: Original lists Don't change


# print("================ Destructive vs Non-Destructive operations =============== ")


print("--------------- Adding Elements --------------- ")
print("--------------- L1+L2 (concatenate)  ")
primes = [2, 3, 5, 7, 11]
print('Original address of primes:', id(primes))

others = [13, 17, 19]
primes = primes + others
print("newPrimes: ", primes)
print('New address of primes:', id(primes))


### one elemnt
#primes = primes + 19
primes = primes+[19]
print(primes)



### L.append(item): Destructive
    #add an item at the end of the same list (in-place) 
print("--------------- L.append(item)  ")
print('address of primes:', id(primes))
primes.append(23)
print(primes)
print('New address of primes:', id(primes))



### L.insert(index, item): Destructive
    #add an item at index of the same list (in place)
print("--------------- L.insert(index, item)")
primes.insert(3,19)
print(primes)

primes.insert(0,19)
print(primes)


### L.extend(seq): Destructive
    #add all items from another list/tuple seq onto the end of  the same list L (in-place)

print("--------------- L.extend(seq)")
primes.extend(others[0:2]) 
print(primes)
t = (31, 37)
primes.extend(t)
print(primes)

########### Deleting Elements
myList = [10, 20, 56, 8, 3, 2, 56, -3]

##L.remove(item): Removal by Content
    #remove the (first) element with value item in the list,
    #Move all the other items in the list down by one index number (in-place) 
    
print("--------------- Deleting Elements: --------------- ")
print("--------------- L.remove(item)")
myList.remove(56)
print(myList)
#myList.remove(9)
if 9 in myList:
    myList.remover(9)
    
    
###L.pop(indx): Removal by Index
    #removes the item present at index position
    #Move all the other items in the list down by one index number (in-place)
    #The removed item is also returned by the function 

print("--------------- L.pop(indx) ")    
i = myList.pop(1)
print(myList)
print(i)

if 10 < len(myList):
    myList.pop(10)

y = myList.pop()
print(myList)
print(y)

#need len() before pop



########### SORTING

    #sorted(seq): works for any sequence (list, tuple, string) 
        #and returns a list which is a sorted copy of the original sequence
        #The original object is not modified

print("--------------- SORTING --------------- ")
L = [-1, 2, 7, 1, -2, 0, 5]

### sorted(seq):Non-DESTRUCTIVE
newL = sorted(L)
print(newL)
print(L)


### sorted(seq, reverse=True), optional 
newL = sorted(L, reverse =  True)
print(newL)
print(L)


### L.sort():DESTRUCTIVE

L.sort()
print(L)

### L.sort(reverse=True), optional 
L.sort(reverse=True)
print(L)


### elements need to be of the same type
L = [2, -4, 'Hello', 11]
#L.sort()


### list of tuples of primitive types
 #sorted according to the first element(s) of each list/tuple
my_tuples = [(1,2), (5,7,8), (-1,), (0,9,1,3)]



########### Reversing

print("--------------- Reversing --------------- ")

## L.reverse():DETSRUCTIVE (in-place)
print(L)
L.reverse()
print(L)


##[::-1]: you obtain a copy of the list L reversed: NON-Destructive (cloning)
newL= L[::-1]
print(newL)
print(L)

########### List Assignment: cloning vs aliasing: SLIDES

print("--------------- List Assignment --------------- ")

# Behavior for basic types

x = 10
y = x
x = x + 1
print("x =", x)
print("y =", y)


X = L #Alias:two names for the same physical list in memory! 

print("L", L)
print("X", X)

L.append(3)
print("L", L)
print("X", X)

print("id x", id(X))
print("id L", id(L))

Y = L[::]  #clone
Z = L.copy() #clone
L.append(5)

print("L", L)
print("Y", Y)
print("Z", Z)

print("id L", id(L))
print("id Y", id(Y))
print("id Z", id(Z))


#print(id(X), id(L), id(Y))


### Cloning 2D Lists

L1 = [[11,12],[21,22],[31,32],[41,42]]
L2 = L1.copy()
L1[0][0] = 100
L1[0] = 2
print("L1 =", L1)
print("L2 =", L2)


### but deepcopy will
import copy
L1 = [[11,12],[21,22],[31,32],[41,42]]

L2 = copy.deepcopy(L1)
L1[0][0] = 100
print("L1 =", L1)
print("L2 =", L2)
