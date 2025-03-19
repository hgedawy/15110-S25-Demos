# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 13:17:58 2025

@author: hkg
"""


def ct2(d, key): 
    while (key in d) and ((key+2) not in d): 
        d[key+2] = key+1 
        key = d[key]
    print(d)
    L = [ ] 
    for key in sorted(d.keys()): 
        L.append(10*key + d[key]) 
    return L 

print(ct2({1:5, 0:2}, 0)) 


def mostFrequent(L):
    # Return most frequent element in L, 
        #resolving ties arbitrarily.
    maxValue = None
    maxCount = 0
    counts = dict()
    for element in L:
        count = 1 + counts.get(element, 0)
        counts[element] = count
        if (count > maxCount):
            maxCount = count
            maxValue = element
    return maxValue


def testMostFrequent():
    print("Testing mostFrequent()... ", end="")
    assert(mostFrequent([2,5,3,4,6,4,2,4,5]) == 4)
    assert(mostFrequent([2,3,4,3,5,3,6,3,7]) == 3)
    assert(mostFrequent([42]) == 42)
    assert(mostFrequent([]) == None)
    print("Passed!")

testMostFrequent()






################################### From Notes
def charFreq(s):

    return ''

# Example usage
message = "Congratulations, Ahmad!"
print(charFreq(message))



def sortByPop(d):

    return []

# Example usage
population_dict = {
    'China': 1409517397,
    'India': 1339180127,
    'United States': 324459463,
    'Indonesia': 263991379,
    'Brazil': 209288278,
    'Pakistan': 197015955,
    'Nigeria': 190886311,
    'Bangladesh': 164669751,
    'Russia': 143989754,
    'Mexico': 129163276
}

print(sortByPop(population_dict))