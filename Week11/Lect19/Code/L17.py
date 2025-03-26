'''
class_110 = { 'Jim': 4.65,
              'Paul': 4.88,
              'Ann':  5.00,
              'John': 3.2,
              'Mariam': 4.91
             }

numbers = { 1: 'r', 
            2: 'p',
            3: 'p',
            4: 'r',
            5: 'p',
            6: 'r'
           }

animals = { 'cat': 'mammal', 
            'dog': 'mammal',
            'bee': 'insect',
            'ant': 'insect',
            'spider': 'arachnid',
            'snake': 'reptile'
           }

accounts = { 64867: ['Jim Smith', 'M', 45, 'USA'],
             43982: ['Tony White', 'M', 28, 'USA'],
             124:   ['Albert Dupont', 'M', 27, 'France'],
             43982: ['Anna Bianchi', 'F', 25, 'Italy']
            }
             
print(class_110['Ann'])  

Jim = class_110['Jim']   

class_110['Ann'] = 4.76    

class_110['Sara'] = 4.53

if 'Sara' in class_110:
    print('Sara\'s grade:', class_110['Sara'])
  
print(class_110.keys())

key_list = list(class_110.keys())

d_empty = dict()
'''
'''
numbers = {32: 'r', 1: 'p', 0:'x', 2: 'p', 
           3:'p', 4:'r', 5:'p', 13:'p',
           6:'r', 36:'r', -1: 'x'}

m_val = max(numbers.values())
print(m_val)

for k in numbers.keys():
    if numbers[k] == m_val:
        print('key of max is:', k)
        break
'''
      
numbers = {32: 'r', 1: 'p', 0:'x', 2: 'p', 
           3:'p', 4:'r', 5:'p', 13:'p',
           6:'r', 36:'r', -1: 'x'}

animal_list = [ ('dog', 'mammal'), ('cat', 'mammal'),
               ('bee', 'insect'), 
               ('spider', 'arachnoid')]

animal_dict = dict(animal_list)

xx = [1, 2, 3, 4, 5, 6]
yy = ['r', 'p', 'p', 'r', 'p', 'r' ]

list_of_words = ["This", "is", "a", "list", "of", "key", "strings"]
dict_of_words = dict.fromkeys(list_of_words, 0) 

primes = [2, 3, 5, 7, 11, 13]
dict_of_primes = dict.fromkeys(primes, 'p')



'''
for k in sorted_n:
    print(k)
'''

'''    
for i in numbers.keys():
    print(i)
  
for i in numbers.values():
    print(i)
    
for i in numbers.items():
    print('Key is:', i[0], 'Value is:', i[1])
'''
 











'''
keys_now_in_dict = list(numbers)

keys_view = numbers.keys()

#L = list(numbers.keys())

print(keys_now_in_dict[3])

keys_now_in_dict[3] = 2

numbers[13] = 'p'


print(keys_view)

print(keys_now_in_dict)
'''

'''
accounts = [ ['J. Smith', [35672, 'M', 'USA']], 
             ['M. Saleh', [27623, 'M', 'Jordan']], 
	          ['F. Dupont', [17623, 'F', 'France']] ]

change_value(accounts, 'M.Saleh', 2, 'Spain')

def chage_value(L, name, index, value):
    for i in range(L):
        if name == L[i][0]:
            L[i][1][index] = value
'''         
 
'''   
numbers = {1: 'p', 2: 'p', 3:'p', 4:'r', 5:'p', 
           6:'r', 7:-1, 99: [0,1,2], 'hana':5 }

#print(numbers[0])

numbers['hana'] = 4

x = numbers['hana']

numbers[2] = 'r'
'''

d = {}

d['Doha'] = 32

d['Tokyo'] = 25

#if 'Tokyo' in d:
#    del d['Tokyo']
    
y = d

y['Rome'] = 27

#y[ ['paris', 'london']] = 18






























