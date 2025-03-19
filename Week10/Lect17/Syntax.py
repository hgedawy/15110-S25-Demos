# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 21:52:49 2025

@author: hkg
"""

############## Motivation


### Familiar from Quiz6
def calculate_grade_distribution_with_lists(grades):
    unique_grades = []
    grade_frequencies = []
    
    for grade in grades:
        if grade in unique_grades:
            index = unique_grades.index(grade)
            grade_frequencies[index] += 1
        else:
            unique_grades.append(grade)
            grade_frequencies.append(1)
    
    return unique_grades, grade_frequencies

# Example usage:
grades = [85, 90, 75, 85, 95, 90, 80, 85, 90]
unique_grades, grade_frequencies =  calculate_grade_distribution_with_lists(grades)
print(f"unique_grades: {unique_grades} ")
print(f"grade_frequencies: {grade_frequencies} ")




# dictionary maps grades to frequency..
def calculate_grade_distribution_with_dict(grades):
    grade_distribution = dict()
    for grade in grades:
        if grade in grade_distribution:
            grade_distribution[grade] += 1
        else:
            grade_distribution[grade] = 1
    return grade_distribution

# Example usage:
grades = [85, 90, 75, 85, 95, 90, 80, 85, 90]
print(calculate_grade_distribution_with_dict(grades))

   

##### Dictionary data structure: non-scalar, mutable, not ordered (i.e. collection not sequence)
#d = { key_1: value_1,  key_2: value_2,  key_3: value_3 } 
#Dictionaries are associative data structures that store key-value pairs ..


############### Number of Items
d = {'John': 22, 'Jim': 20, 'Mary': 20, 'Paul': 29}
print("Number of items: ")
print(len(d))


############### Creating empty dict
print("\nCreating Empty Dict: ")
d2 = {}
ages = dict()
print(ages)

############## Adding and Modifying Entries

print("\nAdding And Modifying Entries =====================: ")

key= "Fatima"
value= 20

d2[key] = value
print(d2)

#if the key already exists, using same syntax will
    #Update value of the existing keys
d['Jim'] = 30
print(d)


#Delete an existing item:
del d["Jim"]
print(d)

#del d["Fatima"]

############### Getting Values

print("\nGetting Values =====================: ")

print(d["Paul"])

#v = d["Fatima"]
#print(v)

### FIX 

#1) check first that it is there 
if "Fatima" in d:
    print(d["Fayima"])
    
#2) Using get method
# d.get(key, <value>)
    #value is the value to return if the specified key is not found in the dict
    #The value parameter is optional. If value is not passed,  None is returned.

v = d.get("Fatima")
print(v)


v = d.get("Fatima", 1)
print(v)

######### Membership Operator

print("\nMembership Operator =====================: ")


#checks for keys by default
if "Mary" in d.keys():
    print("Mary is in keys")

elif "Mary" in d.values():
    print("it is in values")

    



######### Getting Values, Keys, items

phone_numbers = {'Ann': 5461, 'Paul': 5472, 'Mark': 3541, 'Liz': 2451}
numbers = {1: 'r', 2: 'p', 3:'p', 4:'r', 5:'p', 6:'r'}
print("\nGetting Values, Keys, items =====================: ")

print(numbers.keys())
print(phone_numbers.values())
print(numbers.items())

######## Looping Through Dictionary

print("\nLooping Through Keys, values, and pairs =====================: ")

#over keys
for k in d: # d.keys()
    print("key: ", k)

#over values
for v in d.values():
    print("v: ", v)

    
#over all dictionary elements: 
    #pairs (key, value) as tuples
for item in d:
    print("(key, value): ", item[0], item[1] )



################# Keys and Values Types
# A key can only contain immutable data types
    #int, float, bool, str, tuple
# A value can be of any type

print("\nKeys and Values Types =====================: ")

d[12] = 'New data value'
d['Jim'] = True
d['List data'] = [ [1,2,3], [4,5,6] ]
d[(2,3)] = 7.8
print(d)

#Mutable data types for keys!
#d[[2,3]] = 'Incorrect'
#d[([1,3], 2)] = 'Incorrect'


T = (1,2)
d[T] = "Hello"
print(d)

T = T + (5,6)
print(d)

