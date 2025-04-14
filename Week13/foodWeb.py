file = open("florida-foodweb.csv")

foodweb = {}
all_animals = []
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
    if animal in fw:
        return fw[animal]
    else:
        return []
    
predatorsOf("Anchovy", foodweb)
#predatorsOf("Sharks", foodweb)



def preysOf(animal, fw):
    preys = []
    for a in fw:
        if animal in fw[a]:
            preys += [a]
    return preys

preysOf("Sharks", foodweb)


# plant --> goat --> wolf
# { plant: [goat]
#   goat: [wolf]
# }

def producers(fw):
    prod = []
    for possible_producer in fw:
        isProducer = True
        for a in fw:
            if possible_producer in fw[a]:
                isProducer = False

        if isProducer:
            prod += [possible_producer]
            
    return prod

producers(foodweb)


# plant --> goat --> wolf
# { plant: [goat]
#   goat: [wolf]
# }

def apexPredators(fw, aa):
    ap = []
    for a in aa:
        if a not in fw:
            ap += [a]
    return ap
    
apexPredators(foodweb, all_animals)