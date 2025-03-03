# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 12:33:57 2025

@author: hkg
"""

def mystery_1(L):
    L = L+[6]
    return L

def mystery_2():
    global L
    L1= mystery_1(L)
    print(L, L1)
    L.sort()
    return L


L = [10 , 4 , 7]
L2 = mystery_2()
print(L, L2)






######################## Functions as argments ####################
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

# Transform function takes a function f as a parameter
def transform(img, f):
    rows = len(img)
    cols = len(img[0])
    new_img = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            r = img[i][j][0]
            g = img[i][j][1]
            b = img[i][j][2]
            # f is used to transform the previous (r,g,b) value into the new pixel
            new_pixel =  f(r, g, b) #makeTransparent(r,g,b), makeGrayscale(r,g,b), removeRed(r,g,b)
            new_row += [new_pixel]
        new_img += [new_row]
    return new_img

def makeTransparent(r,g,b):
    return (r,g,b,0.75)

def makeGrayscale(r,g,b):
    return 0.3*r + 0.59*g + 0.11*b

def removeRed(r,g,b):
    return (0, g, b)


######### Code for showing the picture ########

# Loads the image
img = imread('doha.jpg') # Change this to a file in your computer so that it works
plt.imshow(img)


# # The function can be called using the function we want
# new_image = transform(img, removeRed)

# # Uncomment to test the transform function
# plt.imshow(new_image)
# # plt.imshow(new_image, cmap="gray") # For grayscale images

# plt.show()
