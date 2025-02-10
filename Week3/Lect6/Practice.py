# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:02:24 2025

@author: hkg
"""

def is_odd(n):
    return False

# Test cases
#print(is_odd(1))  # Expected output: True
#print(is_odd(2))  # Expected output: False
#print(is_odd(0))  # Expected output: False
#print(is_odd(-3)) # Expected output: True



#can use builtin max(a,b)
def max_two_elif(a, b): #with elif
    return 42
    
# Test cases
#print(max_two_elif(3, 5))  # Expected output: 5
#print(max_two_elif(10, 7)) # Expected output: 10
#print(max_two_elif(4, 4))  # Expected output: -1



def max_two(a, b): #without elif
    return 42

# Test cases
#print(max_two(3, 5))  # Expected output: 5
#print(max_two(10, 7)) # Expected output: 10
#print(max_two(4, 4))  # Expected output: -1



def comfortable_weather(t):
    return 42
# Test cases
#print(comfortable_weather(15))  # Expected output: 1
#print(comfortable_weather(10))  # Expected output: 0
#print(comfortable_weather(35))  # Expected output: -1

    

#can use builtin max(a,b, c)
def max_three(a, b, c):
    return 42
# Test cases
#print(max_three(10, 5, 7))  # Expected output: 10
#print(max_three(-1, -2, -3))# Expected output: -1
#print(max_three(0, 0, 0))   # Expected output: 0

    
    
def middle(a, b, c):
    return 42

# Example usage:
#print(middle(1, 2, 3))  # Output: 2
#print(middle(9, 5, 7))  # Output: 7
#print(middle(4, 4, 4))  # Output: 4



def bestCard(c1, c2):
    return 42

# Example usage:
# print(bestCard(5, 5))  # Output: 5 (Three of a Kind)
# print(bestCard(3, 7))  # Output: 7 (Pair with the higher value)
# print(bestCard(10, 2)) # Output: 10 (Pair with the higher value)



def roundNumber(x):
    
    intPart = int(x)
    decPart = x - intPart
    
    if decPart >= 0.5:
        return intPart+1
    
    return intPart
    

# Example usage:
print(roundNumber(99.99))  # Output: 100
print(roundNumber(2.01))   # Output: 2
print(roundNumber(2.5))    # Output: 3
print(roundNumber(2.49))   # Output: 2    
    
    

def winner(game1Team1, game1Team2, game2Team1, game2Team2):
    return ""

# Example usage:
#print(winner(2, 1, 1, 2))  # Output: "Penalty"
#print(winner(3, 1, 1, 2))  # Output: "Team 1"
#print(winner(1, 2, 2, 1))  # Output: "Penalty"
#print(winner(2, 2, 1, 3))  # Output: "Team 2"