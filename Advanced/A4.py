from random import randint

def Cartesian(sets):
    return None

n = 5
sets = []

for i in range(n):
    sets.append([])
    for j in range(randint(1, 20)):
        sets[i].append(randint(1, 20))

for i in range(len(sets)):
    print('Set',i+1,': ',sets[i])


Cartesian(sets)
