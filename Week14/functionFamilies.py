# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 10:32:54 2025

@author: hkg
"""

import time
import matplotlib.pyplot as plt
import math


plt.figure(figsize=(10,6))


xs = []
ys = []
for n in range(1,30):
    xs += [n]
    y = 50
    ys += [y]
plt.plot(xs, ys, 'r', label='constant')


xs = []
ys = []
for n in range(1,30):
    xs += [n]
    y = 400*math.log(n)
    ys += [y]
plt.plot(xs, ys, 'b', label='logarithmic')


xs = []
ys = []
for n in range(1,30):
    xs += [n]
    y = 100*n
    ys += [y]
plt.plot(xs, ys, 'g', label='linear')


xs = []
ys = []
for n in range(1,30):
    xs += [n]
    y = 5*n*n
    ys += [y]
plt.plot(xs, ys, 'c', label='quadratic')


xs = []
ys = []
for n in range(1,30):
    xs += [n]
    y = math.pow(2,n)
    ys += [y]
plt.plot(xs, ys, 'm', label='exponential')


plt.legend(loc="upper right")
plt.ylim((0,2000))
plt.show()