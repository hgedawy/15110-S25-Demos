def numberOfDigits(n): 
    if n == 0:
        return 1
    n = abs(n)
    d = 0
    print('n:',n)

    while n >= 0:
        print('-------')
        print('n - %:', n % 10 )
        n = n // 10
        print('n - //:', n)
        d = d + 1
        print('Iterations:', d)
    return d

def cnt():
    counter = 0
    for i in range(3, 13, 3):
        counter = counter + 1
        print("loop index:", i, counter, 
              'hello!',
              i * i)
        
def too_many_digits():
    v = 1
    for i in range(3, 50, 3):
        v = v + ( v / 2) 
        print("v:", v, v*v, v ** 3)
        
def precision():
    v = 1
    for i in range(3, 50, 3):
        v = v + ( v / 2) 
        print("v:", round(v,3), 
              round(v*v, 2), round(v**3, 2))
     
        
     
def numberOfDigits2(n):
    if n == 0:
        return 1
    n = abs(n)
    p = 0
    while True:
        powers10 = 10 ** p
        print('powers of 10:', powers10, 'p:',p)
        if ( n % powers10 ) == n:
            print('Break at ', p)
            return p
        else:
            p = p +1
  
        
      
      
        
      