# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 09:59:07 2025

@author: hkg
"""

######################## I/O: Print() and Input()


#input w/o arguments
def isInputNumber(): 
    x = input() 
    if x.isdigit(): 
    	return True 
    else: 
    	return False 

print(isInputNumber() )

#input with arguments
n = input('Enter a number: ')
print('You have entered:', n)


### Keep intereacting until a certain condition is met

print('I\'ll make the sum of the number that you will enter!')
print('Enter 0 to end')

numbers = []
while True:
    n = input('Enter a number: ')
    
    if n == '0':
        print('Sum is: ' + str(sum(numbers)))
        break
        
    if n.isnumeric():
        numbers.append(int(n))
    else:
        print('Please enter a valid number!')




######################## Open a filE

#file_handle = open(file_name, <modes>)


#default
f = open('data.txt', 'rt')
print(f)


#File must be in the same folder of the calling program!
        #Otherwise, a path must be specified
f = open('C:/Users/hkg/Box/Hend110_S25/Lectures/wk11/sample.txt')



######################## read() - returns a string with the data read

data = f.read()
print(data)


####### Reading a specific number of bytes (characters) 
    #- 1 byte = 1 char
    #reads at most the current number of bytes from currecnt position

#reopen to go back to the beginning
f = open('C:/Users/hkg/Box/Hend110_S25/Lectures/wk11/sample.txt')
chars= f.read(10)
print(chars)


## getting current position: .tell()
print(f.tell())
print(f.read(10))
print(f.tell())


####### Go to a certain position
f.seek(10)
print(f.tell())
print(f.read(10))
print(f.tell())

f.seek(0) #go to the beginning

######## line by line (record by record)


## .readline()
print(f.readline())
print(f.tell())
print(f.readline())



#or loop through the lines of a file :
f = open('numbers.txt', 'rt')
s = 0
for line in f:
    n = int(line) # We know the line has one int
    s += n
print(s)



####### All Lines into a List: .readlines():

f = open('sample.txt', 'rt')
l = f.readlines()
print(l)

f.seek(0)
for line in f.readlines():
    print(line)


     

######################## WRITING TO Files

f = open('Hello.txt', 'w+') #overwrite
nbytes = f.write('New line: 0 3 5.5\n')
nbytes = f.write('Another new line: 1 2 3\n')
print(nbytes)
f.seek(0)
print(f.readlines()) 



######## Append

f = open('data.txt', 'a+') #append
nbytes = f.write('New line: 0 3 5.5\n')
nbytes = f.write('Another new line: 1 2 3\n')
f.seek(0)
print(f.readlines()) 


########## X: Fails if file exists
    #ensures that you don't accidently overwrite existing file
 
# f = open('data.txt', 'x+')
# nbytes = f.write('New line: 0 3 5.5\n')
# nbytes = f.write('Another new line: 1 2 3\n')
# f.seek(0)
# print(f.readlines())


######################## Close Files
f.close()

######################## CSV Files Excercise: Zoo

# One Way
def readZoo(file_path):
    zoo_dict = {}

    with open(file_path, mode='r') as file:
        #get all lines
        lines = file.readlines()
        #for each line
        for line in lines:
            #Skip line: if it starts with # or is empty line
            if line.startswith('#') or not line:
                continue
            #remove trailing and leading spaces, then create a list of values 
            row = line.strip().split(',') 
            #each line is one new entry in the outer dictionary
                #{animalName: attributesDictionary}
            #key: first value in the list is animal name
            animal_name = row[0]
            # inner dictionary: create dict for attributes 
            attributes = { 
                'hair': int(row[1]),
                'feathers': int(row[2]),
                'eggs': int(row[3]),
                'milk': int(row[4]),
                'airborne': int(row[5]),
                'aquatic': int(row[6]),
                'predator': int(row[7]),
                'toothed': int(row[8]),
                'backbone': int(row[9]),
                'breathes': int(row[10]),
                'venomous': int(row[11]),
                'fins': int(row[12]),
                'legs': int(row[13]),
                'tail': int(row[14]),
                'domestic': int(row[15]),
                'catsize': int(row[16])
            }
            
            #map attribute to animal name
            zoo_dict[animal_name] = attributes 
    return zoo_dict


####### Reading files using the csv library

#the csv.reader function takes as input a file 
    #(which was already opened using the open function), 
    #and returns a reader object. 
    


import csv

def readZoo_csv(file_path):
    zoo_dict = {}
    
    with open(file_path, mode='r') as file:

        robj = csv.read()
        
        for row in robj: # row is a list of strings 
            
            if not row or row[0].startswith("#"):
                continue
            
            #each line is one new entry in the outer dictionary
                #{animalName: attributesDictionary}
            #key: first value in the list is animal name
            animal_name = row[0]
            # inner dictionary: create dict for attributes 
            attributes = { 
                'hair': int(row[1]),
                'feathers': int(row[2]),
                'eggs': int(row[3]),
                'milk': int(row[4]),
                'airborne': int(row[5]),
                'aquatic': int(row[6]),
                'predator': int(row[7]),
                'toothed': int(row[8]),
                'backbone': int(row[9]),
                'breathes': int(row[10]),
                'venomous': int(row[11]),
                'fins': int(row[12]),
                'legs': int(row[13]),
                'tail': int(row[14]),
                'domestic': int(row[15]),
                'catsize': int(row[16])
            }        
    
        zoo_dict[animal_name] = attributes

    return zoo_dict


def mammals_that_lay_eggs(zoo_dict):
    mammals_eggs = []
    for animal, attributes in zoo_dict.items():
        # Check if the animal is a mammal (produces milk) and lays eggs
        if attributes["milk"] == 1 and attributes['eggs'] == 1:
            mammals_eggs.append(animal)
            
            
    return mammals_eggs



def aquatic_mammals(zoo_dict):
    aquatic_mammals_list = []
    for animal, attributes in zoo_dict.items():
        # Check if the animal is a mammal (produces milk) and is aquatic
        if attributes["milk"] == 1 and attributes['aquatic'] == 1:
            aquatic_mammals_list.append(animal)
    return aquatic_mammals_list



def animals_with_five_legs(zoo_dict):
    five_legged_animals = []
    for animal, attributes in zoo_dict.items():
        # Check if the animal has five legs
        if attributes["legs"] == 5:
            five_legged_animals.append(animal)
    return five_legged_animals




# Example usage without CSV library:
zoo_data_no_csv = readZoo('zoo.csv')
print("Mammals that lay eggs (without CSV):", mammals_that_lay_eggs(zoo_data_no_csv))
print("Aquatic mammals (without CSV):", aquatic_mammals(zoo_data_no_csv))
# print("Animals with five legs (without CSV):", animals_with_five_legs(zoo_data_no_csv))



##### Another way to read CSV files
#The csv library DictReader() function reads the file into dictionaries. 
#However, Each line becomes a dictionary whose keys are the column names.
file = open("movies.csv")
csv_dict_reader = csv.DictReader(file, delimiter=",")
print(csv_dict_reader.fieldnames)
for d in csv_dict_reader:
    print(d)
    