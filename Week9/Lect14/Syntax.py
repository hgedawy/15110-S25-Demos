# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 12:48:34 2025

@author: hkg
"""

############## Defining String Data Type

#string is a python datatype, just like int, bool, or list are datatypes. 
#The values of type string are sequences of characters, 
    
### single
'Hello!'
'z'  
'_wow_'


### Double
"Number 5"
"Hello!"


############ Sequence of Chars

#Virtually any character can be included in a string sequence!
'This is a   biZarre   sTRING! *&%^$ _-+@#//>><<}{}[]'


### Case matter
print("Capitalization and spaces matter ===============")

#Capitalization is always respected
su = 'Hello!'
sl = 'hello!' 
print('su == sl? ', su == sl)

### Spaces are characters as others
s =  'Hello!'
sp = 'Hello! ' 
print('s == sp? ', s == sp)


### Triple: multi-line strings
s= '''This is the first line
This is the second line
This is the third line
''' 
print("\nTriple Quotes - multi-line String:")
print(s)


#Printing multi-line string using newline character
s = "This is the first line\nThis is the second line\nThis is the third line"

print("\nPrinting with newline character:")
print(s) 



### Quotes in a String
print("\nQuotes in a String: ")
print('This "trick" is cool!') 
print("This 'trick' is cool!") 

print("This \"trick\" is cool!") #escape sequences
print('This \'trick\' is cool!') 



############ Type: str

print(" \nType Str and Casting =================")
s =  'Hello!'
print('type(s) == str? ', type(s) == str)


########## Casting

#str(x): Returns x converted as a string, x can be virtually anything … 

print(str(10)) # -> '10'
l = [1,2]
sl = str(l)
print(type(sl))

print(str([1,2])) # '[1,2]'
print(type(str(True)) == str) #'True'

###Everything that is printed by python is a string. 
print([1,3]) #→  '[1,3]'



############ String vs Tuples: sequences, non-scalar, immutable

### Sequences: restricted to characters 
'Hello Joe' #each character in the string is paired to a position index


### Non-Scalar?
#individual items or sub-sequences can be accessed using indexing and slicing: [], [:], [::]

print("\nStrings vs Tuples ==========================")

s = 'This is a string of 33 characters'
print('First character (at position index 0):', s[0])
print('6th character (at position index 5):', s[5])
print('Last character of the sequence:', s[-1])
print('Sub-sequence at position indices 7 to 12 (included):', s[7:13])
print('Sub-sequence of characters at even position indices:', s[0::2])


### Immutable:
#can't be changed
s = 'Principles of computing'
x = s[5]
print(x)

#s[0] = 'A'



################ String Operators (Almost like Lists)


### Membership: in, not in
# print("\nMembership: ==============")

s = 'Joe' 
in_hello = s in 'Hello Joe'
in_food = s in 'Yummy meal'
print("in: ", in_hello, in_food)


in_hello = s not in 'Hello Joe'
in_food = s not in 'Yummy meal'
print("not in: ", in_hello, in_food)




### Number of characters
print("\nlen(): ==============")
s = "Principles of Computing"
print(len(s))



### Looping through string (similar to lists)
print("\nLooping: ==============")

# by range of length or 
for i in range(len(s)):
    print(s[i], end = " ")
print()
    
# by character
for c in s:
    print(c, end = " ")
print()
    

    
### + Concatenation:
print("\nConcatenation: ==============")

greet_joe = 'Hello Joe'
comma = ','
greet_mary = ' hello Mary'

greet_joe = greet_joe + comma + greet_mary
print(greet_joe)

s = "Hello"
#s[1] = 'A'
s = s[0]+'A'+s[2:]
print(s)

### * duplication:
print("\nDuplication: ==============")

s = 'Hello'
n = 4
print(s * n)

#cummulative
s4 = n * s
print(s4)


### Negative ints
n = -4
print(n*s)


###Augmented Forms: +=, *=
print("\nAugmented Forms: +=, *=: ==============")

s = 'abc'
s1 = 'defg'
s += s1
print(s)

s *= 3
print(s)



### Comparion Between Strings
print("\nComparisons: ==============")
print('a' < 'z')
print("Hello" > "Hi")


## character Encoding
print("\nCharacter Encoding: ==============")
print(ord('a'), ord('z'))
print(ord('$'))
print(ord('😁'))
print(chr(128513) )


####### Sorting Strings
s = "Principles of Computing"
print("\nSorting: ==============")
print(sorted(s))


####### List TO String & String to List


#s.split(sep): 
    #splits the string s in a list of strings, based on separator string sep. 
        # returns a list of strings. 
        # If sep is not given, all white spaces are removed. 

print("\nLists <> Strings:==============")

print("\nSpit:===")
s = "I am John Smith"
ls = s.split()
print(ls)

s = "I  am    John  Smith"
ls = s.split()
print(ls)

s = "I am: John Smith"
ls = s.split(':')
print(ls)

s = "I am   John    Smith"
ls = s.split(' ')
print(ls)

        
#s.join(seq)
   #seq: iterable object (e.g., tuple, list, dict, set) containing only strings, 
   # returns a string in which the elements of seq are joined by s as separator

print("\nJoin:===")
l = ['1','2','3','4']   
sep = "-"  
s = sep.join(l) 
print(s) 

sep = ''  
s = sep.join(l) 
print(s) 

s = ' '.join(l) 
print(s) 

l = ('1','2','3','4')   
sep = ", "  
s = sep.join(l) 
print(s) 

l = ('This','is','a','story')
sep = " "  
s = sep.join(l) 
print(s) 

s = '123'
sep = 'abc'

print(sep.join(s))

s = 'abc'
sep = '123'
print(sep.join(s))