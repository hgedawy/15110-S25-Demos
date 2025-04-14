file = open("florida-foodweb.csv")

foodweb = {}
all_animals = [] # keeping a list of all animals

# A ---> B
# A is a prey, B is the predator
for line in file:
    if line.startswith("#"):
        continue
    vals = line.strip().split(",")
    prey = vals[0]
    predator = vals[1]
    if prey in foodweb:
        foodweb[prey] += [predator]
    else:
        foodweb[prey] = [predator]
        
    if prey not in all_animals:
        all_animals.append(prey)
    if predator not in all_animals:
        all_animals.append(predator)
        

foodweb["Anchovy"]



def predatorsOf(animal, fw):
    return []
    
print(predatorsOf("Anchovy", foodweb))
#print(predatorsOf("Sharks", foodweb))



def preysOf(animal, fw):
    preys = []
    return preys

print(preysOf("Sharks", foodweb))


# plant --> goat --> wolf
# { plant: [goat]
#   goat: [wolf]
# }

def producers(fw):
    prod = []
            
    return prod

print(producers(foodweb))


# plant --> goat --> wolf
# { plant: [goat]
#   goat: [wolf]
# }

def apexPredators(fw, aa):
    ap = []
    return ap
    
print(apexPredators(foodweb, all_animals))