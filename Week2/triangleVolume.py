# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:47:20 2025

@author: hkg
"""


def area(b, h):
    a = 0.5*b*h        
    return a


def volume(a, l):
    v = a * l
    return v


##### main code 


# Input values 
base = 5 
height = 10 
length = 15 

# Calculate the area of the triangle 
output = area(base, height)  
print('area: ', output)
  
# Calculating volume
output2 = volume(output, length)
print("Volume of the triangular prism:", output2) 


#reusing the function with new parameter values
base2= 7
height2= 10
output3 = area(base2, height2) 
print(output3) 

