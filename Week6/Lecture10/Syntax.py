# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 08:11:09 2025

@author: hkg
"""

#Propoerties: Lists are ordered, mutable (can be changed), and allow duplicate elements.


########### Creating Differet Types of lists
prime = [2, 3, 5, 7, 11]  #ints
even = [2, 4, 6, 8, 10, 12, 14, 16, 18]
irrational = [2.71828, 3.14159, 1.41421] #floats
fruits = ['apple', 'pear', 'banana', 'orange'] #strings
[True, False, False] #booleans


#Lists can be heterogeneous as well (*this is a python particularity*)
# You can do this, but you probably shouldn't...
mix = [-1, 'Hello!', True, 10, 9, 'another string', False]
person_info = ['Donald', 'Trump', 14, 'June', 1946, 'President']

# you can create an empty list, will see later how to add elemts to it
empty_list = []

#list with  one element
one_element_list = [5]  
one_element_list = [5,]

# list of lists
list_of_lists = [[1, 'sedan'], ['Toyota', 'Corolla', 1.8, 2012], [52000]]


########## Accessing Elements (Data) in a List By INDEX


print("\n Accessing Elements (Data) in a List By INDEX ------------")

### Single Element from the front of the list
     #+ve Position index: 0 → 𝑛−1
     
print(even[2])
print(person_info[1])
#print(fruits[10]) 



### Accessing elements from the back of the list
   #-ve Position index: −1 →−𝑛
print(even[-1]) 
print(prime[-3])



### Accessing a single element in a lisit of lists'


### Sublist (Slicing) - returns a new sublist

print("\n Accessing Sublist (SLicing)------------")

##L[from: to] - like range - Subsequence of list elements 

print("\n L[from: to]----")
print(mix[1:4])
print(mix[-3:-4]) 
print(mix[-4:-3]) 


##L[from: to: step] - like range - Subsequence with a stride

print("\n L[from: to: step]----")
print(even[2:10:5])
print(prime[2:10:3])
print(even[2:9:2])

print(prime[-1:-3:-1])


##Slicing can be abbreviated

print("\n Slicing abbreviated ----")
print(even[:4]) #even[0:4]
print(even[2:]) #even[2, lastIndex+1]
    
##Slicing with steps can also be abbreviated
print(even[::2])


################ List Length

print("\n List Length: len(L) ------------")
x = len([3, 5, 7, 11, 13])       
print(x)



################ Find Element in a List - By CONTENT
    #Is that content in the list? If it does, where is it? 


print("\n Find Element in a List - By CONTENT------------")


### Membership: Is that content in the list?
 


print("\n Membership ----")
is_prime = 5 in prime      
print(is_prime)

n = 15
if (n in prime):
    print(n, 'is a prime number!')
else:
    print(n, 'is not a prime number')
          
is_prime = 5 not in prime     
print(is_prime)

### Where is a specific item's (data) position in the list?
L = [1, 4, 7, 0, 9]

##L.index(item) method: return the position index of item in list L 
print(L.index(7))
#print(L.index(10))

##to avoid the crash, check membership first. If it is there, get it's position...

if 10 in L:
    print(L.index(10))



################ Modifying a List

print("\n Modifying a List------------")

##using the [ ] operator to change / reassign value

L[2] = "15110"    
L[-1]  = "Hello"
print(L)      

################ Adding an Element
print("\n Adding an Element------------")

L1 = [1,2]
L2 = [3,4]
print(L1+[0])
print(L1)


L1 = L1+[0]
print(L1)

print(L1+L2)

################ Looping through a list

print("\n Looping through a list------------")
L = [2, 3, 6, -1, 6, 8]

for v in L:
    print(v)

print()    
    
for i in range(len(L)):
    print(L[i])

    
    
################ Tuple: ordered, immutable, allow duplicates
print("\n Tuple------------")

T = (1,2,3,4)
print(T[1])
print(T+(5,6))




