# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 12:24:24 2025

@author: hkg
"""



######################### Keys As Lists

accounts = {'J. Smith': [35672, 'M', 'USA'], 'M. Saleh': [27623, 'M', 'Jordan'], 
	         'F. Dupont': [17623, 'F', 'France'] } 
phone_numbers = {'Ann': 5461, 'Paul': 5472, 'Mark': 3541, 'Liz': 2451}
numbers = {1: 'r', 2: 'p', 3:'p', 4:'r', 5:'p', 6:'r'}



#Typecasting a dictionary to a list returns the list of keys:

### .keys() vs. list()

print("\n  Keys As Lists ------------------------------------------------")    
keys_view = numbers.keys() #view object
print("view object: ", keys_view)
#samething for .values() and .items(): also return view objects

keys_now_in_dict = list(numbers.keys()) #list object
#same as list(numbers), creates a list of keys
print("list object: ", keys_now_in_dict)
    
numbers[13] = 'p'
print(numbers)
print("Is 13 in dict? From static list copy:", (13 in keys_now_in_dict) )
print("Is 13 in dict? From dynamic view:", (13 in keys_view) )
print(keys_view)


######################## Creation of dictionary variables


######## : use a list of tuples + dict()

print("\n  List <> Dict -----------------------------------")    

print(list(numbers)) # list(numbers.keys())


#Getting a list of tuples from dict: list(d.items())
colors = {'Blue': 10, 'Red': 7, 'Green': 15, 'Black': 12}
print(list(colors.items()))


word_list = [ ('Hello', 5), ('this', 4), ('is', 2), ('a', 1), ('list', 4) ]
print(dict(word_list))


Accounts_by_country = dict( [ ('USA', [35672, 'M', 'J. Smith']), 
               	               ('Jordan', [27623, 'M', 'M. Saleh']), 
                                  ('France', [17623, 'F', 'F. Dupont']) ] )

print(Accounts_by_country)






####### zip(key_list, value_list)

##Use two lists of the same length, one containing the keys and pair them up 
    #into a list of tuples
print("\n From Two seperate lists: -------------------------")    


list_of_keys = [4, 1, 3, 2, 6, 5]
list_of_values = ['r', 'r', 'p', 'p', 'r', 'p' ]

ml= list(zip(list_of_keys, list_of_values))
print(dict(ml))



######use list of keys with default values

print("\n with default values: -------------------------")    

list_of_words = ["This", "is", "a", "list", "of", "key", "strings"]
dict_of_words = dict.fromkeys(list_of_words, 0) 
print(dict_of_words)

primes = [2, 3, 5, 7, 11, 13]
dict_of_primes = dict.fromkeys(primes, 'p')
print(dict_of_primes)

    
      
    
######################## Creating Copies & Aliasing

d1 = {"A": 1, "B":2} # all immutable values
d2 = {"A": 1, "B":2, "C":[3,4]} # one mutable value
    
print("\nCreating Copies & Aliases -----------------------------------------") 

y = d1
print(id(y) == id(d1))

#when no mutable values
y2 = d1.copy()
print(id(y2) == id(d1))
y2["A"] = 5
print(d1)

y3 = d2.copy() # shallow
print(id(y3) == id(d2))
print(id(d2["C"]) == id(y3["C"]))

#needed when one+ value is mutable
import copy
y4 = copy.deepcopy(d2)
print(id(y4) == id(d2))
print(id(d2["C"]) == id(y4["C"]))

####################### Arithmatic Operators
#==  Equality operator: check if two dicts have the same values 
print("\nArithmatic Operators -----------------------------------------") 
print( d2 == y3)


#Other relational operators   >, >=, <, <=  do not apply to dictionary operands
#Arithmetic operators such as +, - *, / do not apply to dictionary operands


####################### Useful operations on keys and values: 

print("\nUseful Operations on Keys&Values -----------------------------------") 
numbers = {1: 'r', 2: 'p', 3:'p', 4:'r', 5:'p', 6:'r'}

#### Sorted()

#Get the sorted list of keys from the dictionary

print(sorted(numbers)) #number.keys()

#You can do the same for values and items 
sorted_values = sorted(numbers.values()) 
sorted_dict_list = sorted(numbers.items()) # sorted based on keys 
print(sorted_values)
print(sorted_dict_list)


#### min(), max(),  sum()

max_key_val = max(numbers)   
min_key_val = min(numbers)    

#same as
#max_key_val = max(numbers.keys())     
#min_key_val = min(numbers.keys())  
 
print(max_key_val)
print(min_key_val)

# You can do the same for values
max_values = max(numbers.values())   
min_values = min(numbers.values())
print(max_values)
print(min_values)


key_sum = sum(numbers)
#same as: 
#key_sum = sum(numbers.keys()) 

print(key_sum)


values_sum = sum(colors.values()) # sum(numbers.values())
print(values_sum)


######################## Other methods for accessing and modifying a dictionary: 
    

############# .pop()
#Remove and return dictionary element associated to passed key
    
key = 11
x = numbers.pop(key, None)
if x != None:
 	print('Removed pair (', key, ':', x, ')')
    
# #Advantage over the use of  del and [] operators:
key = 11
# del numbers[key]


############# .popitem()
#Remove and return the last inserted dictionary element

x = numbers.popitem()
if len(numbers) > 0:
    print('Removed the last inserted key-value pair (', x, ')')
    print('New size of the dictionary:', len(numbers))


############# .clear()
#All elements are removed, no values are returned, after the call dict = {}
numbers.clear()
print(len(numbers))


