# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 13:13:52 2025

@author: hkg
"""

def unique_words_n2(text):
    words = text.split() #N
    
    unique_words = []
    for word in words: #N
        if word not in unique_words: #N
            unique_words.append(word) #1
 
    return  unique_words

# Example usage:
text = "hello world hello hello world world"
print(unique_words_n2(text))




def unique_words_n(text):
    words = text.split() #N
    
    d = {}
    for word in words: #N
        d[word] = d.get(word, 0) +1 #1
 
    unique_words = list(d.keys())  #N
    return  unique_words

print(unique_words_n("hello world hello hello world world"))