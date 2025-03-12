# -*- coding: utf-8 -*-
"""
Created on Sat Mar  12 16:20:24 2025

@author: hkg
"""


#None of the functions below modify the string.



############################ s.endswith(<suffix>)
#  returns boolean indicating whether s ends with the specified <suffix>

print("\nendswith, startswith ============================")
s = "crazy bar"
print(s.endswith("bar"))

#s.endswith(<suffix>, <start>, <end>): as above, but
    #the comparison is restricted to substring indicated by <start> and <end>
print(s.endswith("bar", 0, 5))


###############s.startswith(<prefix>):
     #analogous to endswith(), checking if s begins with a given substring
print(s.startswith("cr"))



############################s.count(<sub>):  
    #returns the number of non-overlapping occurrences of substring <sub> in s

print("\ncount ============================")

s = "moo ooh pooh"
print(s.count("oo"))


###s.count(<sub>, <start>, <end>):  
    #searches in the s slice defined by <start> and <end>
print(s.count("oo", 0,7))



############################s.find(<sub>): 
   # returns  first index in s where <sub> is found, -1 if not found

print("\nfind ============================")

s = "crazy bar bar"
ibar= s.find("bar")
istar= s.find("star")
print(ibar)
print(istar)



###s.find(<sub>, <start>, <end>): as above,
    #but the search is restricted to the substring indicated by <start> & <end>
print(s.find("bar", 8, len(s)))


################s.rfind(<sub>):  searches s starting from the end (reversed)
    #such that it returns the highest index in s where the substring <sub> is found,
    #-1 is returned if the substring is not found

print(s.rfind("bar"))

###s.rfind(<sub>, <start>, <end>): as above, but now the search is 
    #restricted to the substring indicated by <start> and <end>
print(s.rfind("bar", 0, 8))



############################s.replace(<old>, <new>):  
    #returns a copy of s with all occurrences of substring <old> replaced by new.
        #If there are no occurrence of <old>, 
        #the copy is identical to the original (but it’s still a different object) 

print("\nreplace ============================")

s = "one step, two steps, three steps"
s1= s.replace ("step", "stop") #capitalization matters
print(s1)

##s.replace(<old>, <new>, <max>): as above, but now the number of replacements
    # is limited to the <max> value -- replaces only first n values
s2= s.replace("step", "stop", 2)
print(s2)

print(s)


############################ String Formatting

#s.strip([<chars>]): removes all leading and trailing whitespaces of a string
# also used to remove a particular character 

print("\nformatting ============================")

s= '  Hello  ' 
s1= s.strip()
print(s1)

s='**Hello**'
s2= s.strip('*')
print(s2)




############################ Character Classification
#s.isalpha(): True if all chars in s are alphabetic letters, False otherwise 
#s.isalnum(): True if all chars in s are alphabetic letters or numeric digits
#s.isdigit(): True if all chars in s are numeric digits, False otherwise 
#s.islower(): True if all chars in s are lower case, False otherwise 
#s.isupper(): True if all chars in s are upper case, False otherwise 

print("\ncharacter classification ============================")

a = "hello1"
b = "23"
print(a.isalpha())
print(a.isalnum())
print(b.isdigit())
print(a.islower())
print(a.isupper())

############################ Case Change

#s.upper(): returns a copy of s with all alphabetic chars converted to uppercase

print("\ncase change ============================")

s = "1984 is a dystopian novel by English novelist George Orwell."
sU = s.upper()
print(sU)

#s.lower(): returns a copy of s with all alphabetic chars converted to lowercase
sl = s.lower()
print(sl)



