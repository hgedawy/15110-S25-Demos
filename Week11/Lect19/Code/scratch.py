def sum_first():
  s = 0
  for i in 1,2,3,4,5,6,7,8,9,10:
     s = s + i
  return s

def sum_first():
  s = 0
  for i in 1,2,3,4,5,6,7,8,9,10:
     s = s + i
  return s

def is_odd(n):
    if n % 2 == 0:
        return False
    else:
        return False
    
    
def isEvenPositiveInt(n):
    if (n >= 0) and ( (n % 2) == 0) and (type(n) == int):
        return True
    else:
        return False
    
def letterGrade(pts, total):

    p = 100 * pts / total
    if p >= 90:
        return "A"
    elif p >= 80:
        return "B"
    elif p >= 70:
        return "C"
    elif p >= 60:
        return "D"
    else:
        return "F"


#### setKthDigit ####

def setKthDigit(n, k, d):
    if ((n // (10**k)) % 10) == 0:
        print("Index out of range")
        return False
    
    isNegative = (n < 0)
    n = abs(n)
    a = (n // 10**k) % 10
    n -= a * 10**k
    n += d * 10**k
    if (isNegative):
        n = -n
    return n


#### canGetA ####

def canGetA(pts, graded, total):
    missing = total - graded
    a = total * 0.9
    if missing + pts >= a:
        return True
    else:
        return False


#### leapYear ####

def leapYear(y):
    if y % 4 == 0:
        if y % 100 != 0 or y % 400 == 0:
            return True
        else:
            return False
    else:
        return False

#### calculateAge ####

def calculateAge(bd, bm, by, d, m, y):
    age = y - by
    if bm > m or (bm == m and bd > d):
        age = age - 1
    return age


def print_numbers ():
  for i in True, 2.5, 99.1, False:
     print(i)

def sum_first():
  s = 0
  for i in 1,2,3,4,5,6,7,8,9,10:
     s = s + i
  return s

def sum_all(r_min, r_max):
    s = 0
    for i in range(r_min, r_max+1):
        s = s + i
    return s
     
def sum_odds(r_min, r_max):
    s = 0
    for i in range(r_min, r_max+1):
        if i % 2 != 0:
            s = s + i
    return s
 
 # we know that r_min is an odd number
def sum_odds(r_min, r_max):
    s = 0
    for i in range(r_min, r_max+1, 2):
        s = s + i
    return s
    
    
    
a = 3
b = 10
s = 0
for i in range(a, b+1, 2):
    s = s + i
print(s)
print(i)

a = 3
b = 10
s = 0
for i in range(a, b+1, 2):
    s = s + i
    i = 2 * i
print(s)
print(i)


   
#%% 
import math
 
   
def sum_odds_general(r_min, r_max):
    s = 0
    r_min = math.floor(r_min)
    r_max = math.ceil(r_max)
    print(r_min, r_max)
    
    if r_min % 2 == 0:
        start = r_min + 1
    else:
        start = r_min
        
    for i in range(start, r_max+1, 2):
        s = s + i
    return s

a = sum_all(2, 7)
#%%

def alternatingSum(n):
    
    s_pos = 0
    for i in range(2, n+1, 2):
        s_pos = s_pos + i
        
    s_neg = 0
    for j in range(1, n+1, 2):
        s_neg = s_neg + j

    return s_pos - s_neg



def alternatingSum(n):
    s = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            s = s + i
        else:
            s = s - i 
    return s

def sum_if_divisible(a, b):
    s = 0
    for v in range(a, b+1):
        if (v % 2 == 0) or (v % 3 == 0):
            s = s + v
    return s
        
def isPerfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s = s + i
    if s == n:
        return True
    else:
        return False


def Fibonacci(a1, a2, n):
    print(1, a1)
    print(2, a2)
    for i in range(2, n+1):
        current = a1 + a2
        a1 = a2
        a2 = current
        print(i, current)