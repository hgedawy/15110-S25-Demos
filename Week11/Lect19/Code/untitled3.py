'''
odd = [1,3,5,7]
print(id(odd))

numbers = odd

print(id(numbers))

numbers += [9]
print(id(numbers))

odd = [1,3,5,7]
b = odd.copy()

b[1] = -5

print( id(b), id(odd))
'''

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWZ'

def hana(T,n):
    decode = ''
    for i in range(len(T)):   
        x = ord(T[i])
        y = x-n
        j = chr(y)
        print(T[i], j)
        ns += j
    return ns


def signalDownsampling(signal):
    
    samples_n = len(signal)
    if samples_n < 3:
        return None
    
    peaks = []
    mean_amplitude = signal[0]
    
    if signal[1] < signal[0]:
        peaks.append( (0, signal[0]))
    
    
    for i in range(1, samples_n-1):
        print(i)
        if (signal[i] > signal[i-1]) and (signal[i] > signal[i+1]):
            peaks.append( (i, signal[i]))
        mean_amplitude += signal[i]
        
    if signal[-1] > signal[samples_n-2]:
        peaks.append( (samples_n-1, signal[-1]))
    mean_amplitude += signal[-1]        
    
    return peaks, round(mean_amplitude/samples_n, 1)

def get_median(l):
    l_copy = l.copy()
    l_copy.sort()
    return l_copy[len(l_copy)//2]

def listDiscount(L, discount):
    median = get_median(L)
    for i in range(len(L)):
        L[i] = L[i] * discount
    return (L, median)



x = 5
def f():
    return x + 5

L = [1,2,3,3]

def mean(L):
    return sum(L)/len(L)
    
def mode(L):
    
    most_frequent = (L[0], L.count(L[0]))
    for i in L[1:]:
        if L.count(i) > most_frequent[1]:
            most_frequent = (i, L.count(i))
    return most_frequent[0]

def getStats():
    return (mean(L), mode(L))    

def is_between_min_and_max(x, L, xmin, xmax):
    n = L.count(x)
    if n >=xmin and n <= xmax:
        return True
    else:
        return False
    
def shortFrequency(L=[], n_min=1, n_max=3):
    print('L', L)
    selected = []
    for i in L:
        if i not in selected:
            if is_between_min_and_max(i, L, n_min, n_max):    
                selected.append(i)
    return selected


L__ = [0, 1, 2]
x = 0.5

def mystery_check(a, b):
    return a > b + x

def mystery_compute(a):
    s = 0
    for i in range(len(L)):
        s = s + a[i] * L[i]
    return s
      
def mystery(LL, n=-1):
    if mystery_check(n, LL[0]):
        LL.append(n)
    else:
        LL.append(mystery_compute(L))
    return LL


            
def simpleSubseqMatch(sequence, subseq):
    count = 0
    check = []
    for i in range(len(sequence)):
        if subseq[0] == sequence[i]:
            v = 0
            for j in range (i, len(sequence)):
                check.append(sequence[j])
                v += 1
                if v == len(subseq):
                    break
        if check == subseq:
            count += 1
        check = []
    return count

#L = [1, [3, 4, 6, 8], 5,7]
#print(L)

def nested(L):
    n=len(L)
    for i in range (n):
        print (L[i])

def printNestedLists(L):
    if type(L) == list() or type(L) == tuple():
        print(L[:])
    else:
        print (L)
        
def printNestedLists2(L):
    for v in L: 
        if (type(v) == list) or (type(v) == tuple):
            for i in v: 
                print(i)
        else: 
            print(v)
            
def printNestedLists3(L):
    for i in range( len(L)): 
        if (type(L[i]) == list) or (type(L[i]) == tuple):
            for j in range( len(L[i])): 
                print(L[i][j])
        else: 
            print(L[i])

def fibonacci(n):
    a=0
    b=1
    print(0)
    print (1)
    for i in ran_ge (0,n-2):
        s=a+b
        print(s)
        a=b
        b=s
    
def operations(L, n):
    LL = L[1::2]  
    LL = LL + L[0::2]
    if len(LL) < n:
        print("Short list!")
    return LL
