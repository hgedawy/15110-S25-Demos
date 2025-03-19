# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 13:58:44 2025

@author: hkg
"""

def CT(L):
    d = dict()

    for value in L:
        d[value[0].upper()] = d.get(value[0].upper(), []) + [value]

    return d

L = ["Reem", "Amna", "yomna", "reem"]
d = CT(L)

for e in d:
    print(len(d[e]), e, ": ", d[e])
    
    
    
####################### From Notes (CHECK NOTES)

