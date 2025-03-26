
odd = [1,3,5,7]

def nonDecreasing(L):
    L.sort()
    return L # sorted(L)

x = [5,6,8,2,1,9,9]

y = nonDecreasing(x)

#print('y:', y, '\nx:', x)


def mysteryy(x, s, y, t):
    a = x[s:y:t]
    b = len(x)
    c = []
    for i in range(y,b):
        d = x[i]
        c = c + [d]
    return a + c


def times10(L):
    L10 = []
    for i in L:
       L10 += [i * 10] 
    return L10

def times10_overwrite(L):
    for i in range(len(L)):
       L[i] = L[i] * 10 
    return L


def max_min(L):
    return max(L), min(L)

def count(L,e):
    return L.count(e)

def count_loop(L,e):
    cnt = 0
    for x in L:
        if x == e:
            cnt += 1
    return cnt

def sameLists(L1, L2):
    if L1 == L2:
        return True
    else:
        return False
  
def allTheSame(L):
    s = L[0]
    for v in L[1:]:
        if v != s:
            return False
    return True

def allTheSame(L):
    if min(L) == max(L):
        return True
    else:
        return False
    
def allTheSame(L):
    s = L[0]
    if L.count(s) == len(L):
        return True
    else:
        return False

def allTheSame(L):
    if sorted(L) == sorted(L, reverse=True):
        return True
    else:
        return False


def nonDecreasing_new(L):
    return sorted(L)

def nonIncreasing(L):
    L.sort(reverse=True)
    return L

def nonIncreasing_new(L):
    return sorted(L, reverse=True)


def listProdSum(L):
    list_sum = []
    prod = 1
    for x in L:
        if type(x) == int or type(x) == float:
            prod = prod * x
            list_sum.append(x)
    return (sum(list_sum), prod)


def mystery(M):
    N = []
    a = len(M)
    b = len(M[0])
    for i in range(b):
        x = []
        for j in range(a):
             x.append(M[j][i])

             x.append(M[j][i])
             x.pop(-1)             

        print("x =", x)
             
        N.append([x])
    return N

def noRepeats(L, repeatOK):
    if repeatOK:
        return L.copy()
    else:
        R = [L[0]]
        for e in L[1:]:
            if R[-1] != e:
                R += [e]
        return R
    

    
d = { 1:'r', 2: 'p', 3:'p', 4:'r'}

#d[13] = 'p'
    
d.keys()
    
#for k in d.items():
#    print('Key:', k[0], 'data:', k[1])
    
    

dd = { 1:'r', 2: 'p', 3:'p', 4:'rr'}#, 5:'p'}
    
def is_value_in(v,d):
    if v in d.values():
        return True
    else:
        return False
    
    
du = {0: 'ghg', 567: 'iii', -1: 'oo', 2: 'kk'}  
    
x = [1,2,3,4]
y = [-9, -8, 7]


L = ['a', 'b', 'a', 'b', 'b', 'c', 'z']
    
    
def count(L):
    d = dict.fromkeys(L, 0)
    for k in d:
        d[k] = L.count(k)
    return d
    
def get_middle(d):
    sorted_keys = sorted(d)
    middle_key = sorted_keys[ len(sorted_keys) // 2]
    return d[middle_key]
    
    
    
    
    
    
    
    
    