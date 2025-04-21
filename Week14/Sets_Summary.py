
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 13:01:34 2025

@author: hkg
"""

### Creating a set


# empty set
es= set()
print(es)

# statically allocated set
s3= {1, 2, 3, 3, "A", "B"}
print(s3)

# ### set elements are unordered
# L1 = [1,2,3,4]
# L2= [1,3,2,4]
# print(L1==L2) # False (lists are ordered)

# s4= set(L1)
# s5= set(L2)
# print(s4==s5) # True


# #print(s3[0]) # can't index sets

# ### set elements are immutable
# s3= {1, 2, 3, 3, "A", "B"} #, [1,2]} # a list can't be a set element
# print(s3)
# print(hash("Hello"))

# ### Iterarting over elements & Membership
# for e in s3:
#     print(e)
    
# print(1 in s3)
# print(2 not in s3)

# ### Adding Elements
# s3.add("C") # single element
# print(s3)


# ### Removing elements
# s3.remove(1)
# print(s3)

#s3.remove(1) # throws error if element doesn't exist
#print(s3)


# s3.clear() # removes all elements
# print(s3)
