
'''
def fair_share(items_number, people):
    each_person_share = items_number // people
    print('Share per person', each_person_share)
    remaining = items_number - (people * each_person_share)
    return remaining
'''

def is_odd(n):
    if (n % 2) != 0:
        return True
    else:
        return False
    
    
def max_two(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return -1
   
x = 5
if 2 <= x <= 6:
    print('y')
else:
    print('n')

# 0 1 2 3 4 5 6 7 8 9 10 11 12    
    
def sum_n(n):
    s = 0
    for i in range(n):
        print('Value of i:', i)
        s = s + i    
    return s

def sum_m_n(n, m):
    s = 0
    for i in range(n+1):
        #print('Value of i:', i)
        s = s + i  
    ss = 0    
    for i in range(m+1):
        #print('Value of i:', i)
        ss = ss + i 
        
    return s - ss

#for i in range(5, 1, -1):
#    print('i:',i)
    

def mystery(n):
  a = 1
  b = 1
  for i in range(0, n+1, 2):
    print('i:', i)
    c = (b * (n+1-i))
    d = c // (i+1)
    a = a + d
    b = d
  return a

print(mystery(1))
print(mystery(3))
print(mystery(4))
    
def countMultiplesButNotEven(m, a, b):
    c = 0
    for i in range(a,b+1):
        if (i % m == 0) and (i % 2 != 0):
          c += 1
    return c
    

def isPositive(n):
    return (n > 0)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    