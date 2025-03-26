

#primes = [2, 3, 5, 7, 11, 13]
#primes2 = [17, 19, 23]

#primes = primes + primes2

'''
primes = [2, 3, 5, 7, 11, 13]
print('Original address of primes:', id(primes))

primes2 = [17, 19, 23]
xyz = primes + primes2

print('New address of primes:', id(primes))

primes = [2, 3, 5, 7, 11, 13]
primes = primes

for i in range( len(primes)):
    primes[i] += 17


primes = [2, 3, 5, 7, 11, 13]
print(id(primes))

primes.append(17)
primes.append(19)

print(id(primes))
'''
'''
p = [2, 3, 5, 7, 11, 13]
#p.remove(15)

if 15 in p:
    p.remove(15)
else:
    print('15 not in list!')

if len(p) > 8:
    p.pop(8)
else:
    print('8 not in list')
'''

p = [2, 3, 5, 7, 5, 11, 13, 5, 5]

n = p.index(5)
print(n)

nn = p[n+1:].index(5)

print(n, n+nn+1)





#primes = [2, 3, 5, 7, 11, 13]
#primes = primes + [17]


#primes = [2, 3, 5, 7, 11, 13, 17]
#primes.append(19)

#primes = [2, 3, 5, 7, 11, 13, 17]
#primes.insert(3,19) 

#primes = [2, 3, 5, 7, 11, 13, 17]
#primes.insert(0,19)

#primes = [2, 3, 5, 7, 11, 13, 17]
#other_primes = (19, 23, 29)

#primes.extend(other_primes) 
#primes.extend(other_primes[0:2])

#numbers = [1, 3, 5, 4, 5, 5, 17]

#numbers.remove(5) 