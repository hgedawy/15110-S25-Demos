def sum_first(n):
    s = 0
    k = 0
    for i in range(0, n+1, 7):
        s = s + i
        k = k + 1
        print('i', i)
    print(k, i)
    return s
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

def sum_first_10():
    i = 0
    s = 0
    while i <= 10:
        s = s + i
        print(i)
        i = i + 1
        
    print('Out of while loop!', i)
    return s






def sumUpToMax(max_value):
    sum_n = 0
    n = 1
    while sum_n < max_value: 
        sum_n = sum_n + n
        n = n + 1
    print(sum_n)
    return n-1, sum_n






def decreaseTemperature(t, hot, cooling_step):
    step_num = 0
    while t > hot:
        t = t - cooling_step
        step_num = step_num + 1
    print('Cooling steps: ', step_num) 
    return t




n = 0
sum_n = 0
while True:
    if sum_n + n > 12:
        break
    else:
        sum_n = sum_n + n
        n = n + 1
print('Sum is:', sum_n, 'n is:', n-1)

n = 0
sum_n = 0
while sum_n <= 12:
    sum_n = sum_n + n
    n = n + 1
print('Sum is:', sum_n - (n-1), 'n is:', n-2)
