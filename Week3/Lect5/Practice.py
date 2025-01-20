# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 09:23:48 2025

@author: hkg

"""

import math

def circle_area_round(r):
    return 42

#radius = 5
#print("The area of the circle with radius", radius, "rounded down is ", circle_area_round(radius))



def pythagoras(a, b):
    return 42

#side_a = 3
#side_b = 4
#print("The square of the length of the hypotenuse is", pythagoras(side_a, side_b))



def fair_sharing(items, people):
    return 42

#total_items = 10
#total_people = 3
#print("Each person gets ",  fair_sharing(total_items, total_people), " items.")



def my_watch(now, hrs):
    return 42

#current_hour = 10
#hours_in_future = 7
#print("The hour in the future is", my_watch(current_hour, hours_in_future))



def celciusToFahrenheit(c):
    return 42

#celsius_temp = 25
#print(celsius_temp, "°C is ", celciusToFahrenheit(celsius_temp), " °F")



def fahrenheitToCelcius(f):
    return 42

#fahrenheit_temp = 77
#print(fahrenheit_temp, "°F is ", fahrenheitToCelcius(fahrenheit_temp), " °C")



def bmi(pounds, inches):
    #converted w pounds to kg
    w_kg = pounds * 0.453
    
    #converted h inches to m
    h_m = inches * 0.0254
    
    return w_kg / (h_m **2)

weight_pounds = 150
height_inches = 65
print("The BMI is ", bmi(weight_pounds, height_inches))



def getColor(r1, g1, b1, r2, g2, b2, midpoints, n):
    # Calculate the step size for each color component
    step_r = (r2 - r1) / (midpoints + 1)
    step_g = (g2 - g1) / (midpoints + 1)
    step_b = (b2 - b1) / (midpoints + 1)
    
    # Calculate the RGB values of the n-th color
    r_n = round(r1 + step_r * n)
    g_n = round(g1 + step_g * n)
    b_n = round(b1 + step_b * n)
    
    return (r_n, g_n, b_n)


print(getColor(220, 20, 60, 189, 252, 201, 3, 1))  # Output: (212, 78, 95)



def straggler(fast, slow):
    return 42

#print(straggler(5, 7))  # Output: 3