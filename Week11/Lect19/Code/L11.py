L = [1, 3, 5, 7, 11]

mix = [-1, 'Hello!', True, 10, 9, 'another string', False]

if (10 in L):
    pos = L.index(10)
else:
    print('10 is not in list')
    
prime_numbers = [1, 3, 5, 7, 11]

n = 15
if (n in prime_numbers):
     print(n, 'is a prime number!')
else:
    print(n, 'is not a prime number')

L = [2, 3, 6, -1, 6, 8]
pos_index = 0
for v in L:
    print('List element at position', pos_index, 
          'has value', v)
    pos_index += 1

mix = [2, 3, [5, 7, 9],"hello", 11 ]

x=  mix[-1:0:1]