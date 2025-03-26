
#%%
def sum_first():
  s = 0
  for i in 1,2,3,4,5:
     s = s + i
  return s

def print_n():
  for i in 1,True, 3, -6, 0, 'Hello':
     #s = s + i
     print(i)
#%%




# 7: Sequences of things?
#%%
def print_numbers():
  for i in 1, 2.5, 99.1, -2, 0:
    print(i)
#%%



#%%
def print_mix():
  for i in True, 2.5, 99.1, False:
     print(i)
#%%





# 8: range() function
#%%
def happy_bday(n):
  for i in range(n):
     print(i)
     print('Happy birthday!')
#%%



#%%
def happy_bday(n):
  for i in 0, 1, 2, ..., n-1:
     print('Happy birthday!-')
#%%





# 9: range() function
#%%
def sum_first(n):
  s = 0
  for i in range(n+1):
     print(i)
     #s = s + i
  return s
#%%





# 10: range(start,end,step)
#%%
s = 0
for i in range(1, 10, 2):
     print('Loop variable:', i)
     s = s + i
print('Sum:', s)
#%%



#%%
s = 0
for i in range(-2, 10, 2):
     print('Loop variable:', i)
     s = s + i
print('Sum:', s)
#%%



#%%
s = 0
for i in range(0, 10, 5):
     print('Loop variable:', i)
     s = s + i
print('Sum:', s)
#%%




#%%
s = 0
for i in range(-5, 11, 5):
     print('Loop variable:', i)
     s = s + i
print('Sum:', s)
#%%



# 11: range(end), start from 0, steps of 1
#%%
s = 0
for i in range(5):
     print('Loop variable:', i)
     s = s + i
print('Sum:', s)
#%%



#%%
s = 0
for i in range(0, 5, 1):
     print('Loop variable:', i)
     s = s + i
print('Sum:', s)
#%%



#%%
s = 0
for i in range(10):
     print('Loop variable:', i)
     s = s + i
print('Sum:', s)
#%%


# 12: range(start,end), steps of 1
#%%
s = 0
for i in range(10, 15):
     print('Loop variable:', i)
     s = s + i
print('Sum:', s)
#%%




#%%
s = 0
for i in range(-10, 1):
     print('Loop variable:', i)
     s = s + i
print('Sum:', s)
#%%



#%%
s = 0
for i in range(10, 15, 1):
     print('Loop variable:', i)
     s = s + i
print('Sum:', s)
#%%


# 13: range(start,end,back_steps), start > end
#%%
s = 0
for i in range(10, 5, -1):
     print('Loop variable:', i)
     s = s + i
print('Sum:', s)
#%%



#%%
s = 0
for i in range(20, 12, -2):
     print('Loop variable:', i)
     s = s + i
print('Sum:', s)
#%%



#%%
s = 0
for i in range(0, -5, -1):
     print('Loop variable:', i)
     s = s + i
print('Sum:', s)
#%%


#%%
s = 0
for i in range(10, 5):
     print('Loop variable:', i)
     s = s + i
print('Sum:', s)
#%%


#%%
def sum_range(r_min, r_max):
    s = 0
    for i in range(r_min, r_max+1):
        if i % 2 != 0:
            s = s + i
    return s

#%%










