import math
def number_of_digits(n):
    '''
        n: integer > 0
        Observe: log10(1) is 0, log10(10) is 1, log10(100) is 2, 
        log10(1000) is 3 ...
    '''
    return math.floor( math.log10(n)) + 1

def number_of_digits(n):
    'counts the number of digits'
    return len(str(n))

def number_of_digits(n):
    count = 1
    digit = n
    while True:
        digit //= 10   
        if digit == 0:
            return count
        else:
            count += 1

def get_kth_digit(n, k):
    n = abs(n)
    n = n // 10 ** k
    return n % 10


    
def is_armstrong(n):
    n_digits = number_of_digits(n) 
    power_sum = 0
    for k in range(n_digits):
        digit = get_kth_digit(n, k)
        power_sum += digit ** n_digits
    if power_sum == n:
        return True
    else:
        return False
        

'''
        A number is armstrong if the sum of nth power of digits equals to the number itself.
        First armstrong numbers: 0, 1, ..., 9, 153, 370, 371, 407
    '''
    
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n): 
        if n % i == 0:
            return False
    return True

'''
        Here we define a special number as being either a prime or an armstrong number
    '''
    
def is_special_number(n):
    
    prime, armstrong = False, False
    if is_prime(n):
        print(n, 'is prime!')
        prime = True
        
    if is_armstrong(n):
        print(n, 'is armstrong!')
        armstrong = True
        
    if prime or armstrong:
        return True
    else:
        return False
    
    
    
import math

def quadratic_roots(a = 1, b = -3, c = 2):
    d = 1 / (2 * a)
    sqr = math.sqrt(b**2 - (4 * a *c)) 
    return (-b + sqr) * d, (-b - sqr) * d

def square():
    sizeh = 22
    sizev = 10
    for i in range(sizeh):
        print('-', end ='')
    print()
    for i in range(sizev):
        print('|', end = '')
        for j in range(sizeh-2):
            print(' ', end = '')
        print('|', end = '')
        print()
    for i in range(sizeh):
        print('-', end ='')
    print('\n')
             
    
    
def average(L):
    '''
    Parameters
    ----------
    L : List of numbers

    Returns
    -------
    avg : float, the average of the input list
    '''
    n_elements = len(L)
    avg = sum(L) / n_elements
    return avg

def average_global(): 
    global L
    n_elements = len(L)
    avg = sum(L) / n_elements
    return avg

#x = average([1,2,3])
#x += avg



import matplotlib
from matplotlib import pyplot as plt
import numpy as np

def parabola(x):
    return -x*x + 2

def cubic(x):
    return x*x*x + 2*x*x

def geometric(x):
    return 1 / (1-x)

def line(x):
    return x


def plot_fun(x, f, label, color='b'):
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(x, f(x), label=label, color=color)
    plt.legend()
    plt.show()
    
    
def estimate_max_in_interval(f, 
                             xmin, xmax,
                             samples):
    x = xmin
    step = (xmax - xmin) / samples
    max_val = f(xmin)
    for i in range(samples):
        y = f(x)
        if y > max_val:
            max_val = y
        x += step
    return max_val




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    