#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 21:34:39 2021

@author: giannidicaro
"""

import random
aa = random.sample(range(1, 10), 5)

b = random.choices(range(1,10), k = 9)

def gen_numeric_list(min_size = 0, max_size = 30, min_val = -10, max_val=50):
    length = random.randint(min_size, max_size)
    return random.choices( range(min_val, max_val), k = length)

def mystery(M):
    N = []
    a = len(M)
    b = len(M[0])
    
    for i in range(b):
        x = []
        for j in range(a):
            x.append(M[j][i])
            
            
            x.append(M[j][i])
            x.pop(-1)
            
        print("x =", x)
        N.append([x])
    return N

def getMiddle(l):
    import math
    x = len(l)
    if l == []:
        return None
    if x % 2 == 0:
        y = (x // 2) 
        h = l[y-1]
        return [h, True] 
    elif x % 2 != 0:
        y = x / 2
        y2 = math.ceil(y)
        h = l[y2-1]
        return [h, False]
    
def repeated(L): 
    unique = []
    for e in L:
        if e not in unique:
            unique += [e]
    repeated = 0
    for i in unique:
        if L.count(i) > 1:
            repeated += 1
    return repeated


def simpleSubseqMatch(sequence, subseq):
    c = 0
    a = len(subseq)
    for i in range(len(sequence)):
        if sequence[i] == subseq[0]:
            if sequence[i:i + a] == subseq:
                c += 1
    return c
