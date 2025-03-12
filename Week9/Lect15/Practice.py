# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 14:21:34 2025

@author: hkg
"""


def ct2(s):
    result = ""
    i = 0
    for c in s:
        if c.isdigit():
            result += s[int(c)]
        elif c == c.upper():
            i += 3
        else:
            result += s[i % 2]
        i += 1
    return result

s = "x3Y5cA"
print(ct2(s)) 


def wordCanBeBuilt(s1, s2):
    return False

print(wordCanBeBuilt("water", "rate")) #"rater", "tear", "at"



    
def leastFrequentLetters(s):
    
    return ""

print(leastFrequentLetters("aDq efQ? FB'daf!!!"))

############################ Notes

def countOverlapping(s, ss):
    return 42

# Example usage
print(countOverlapping("AAA", "AA"))  # Output: 2


def fix(M):
    return ""

# Example usage
M1 = "it is already halfway thru the semester and u have no idea what is going on? rest assured u are not alone!a lot of ppl go thru the same desperation ofc.What u need to do is take a step back and figure out what u don't understand and why...it is not 2 l8 to recover. U can do this"
print(fix(M1))

############################ SLIDES
def problem1(text, character):
       
    splitted= text.split()

    for s in splitted:
        if s.startswith(character):
            print(s.lstrip(character))
            
            
            

def problem2(sentence):
    splitted= sentence.split()
    titlesList=[]
    
    for s in splitted:
        if s.isupper(): 
            print(s)
            titlesList.append(s.title())
        if s.isdigit():
            print(s)
            
    titlesString=','.join(titlesList)
    print('Titles Are:', titlesString)
    
    

def problem3 (repetitiveString):
    uniqueStringsCombined=""
    
    repetitiveSplitted= repetitiveString.split(' ,')
    
    for s in repetitiveSplitted:
        if not s in uniqueStringsCombined:
            print(s,':',repetitiveString.count(s))
            uniqueStringsCombined+= (s+' ')
            
    print('Unique Text: ', uniqueStringsCombined)
    
    
    
def problem3WithJoin (repetitiveString):
    uniqueStrings=[]
    
    repetitiveSplitted= repetitiveString.split(' ,')

    for s in repetitiveSplitted:
        if not s in uniqueStrings:
            print(s,':',repetitiveString.count(s))
            uniqueStrings.append(s)
            
    uniqueStringsCombined= ' '.join(uniqueStrings)
    print('Unique Text: ', uniqueStringsCombined)
