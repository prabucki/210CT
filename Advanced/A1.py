

def AlienInvasion(x, y, days):
    day = 1
    aliens = 1
    HatchedEggs = {} # key = days for egg to hatch, value = number of eggs

    for i in range(y+1):
        HatchedEggs[i] = 0

    while day<=30:
        aliens += HatchedEggs[0]
        HatchedEggs[y] = aliens * x
        for i in range(1, y + 1):
            HatchedEggs[i-1] = HatchedEggs[i]
        print('After day', day,': ', aliens, 'aliens, ', HatchedEggs[y], 'hatched eggs today')
        day += 1
    return aliens

x = 3 # Eggs alien lays each day
y = 5 # Days after egg hatches
days = 30

print(AlienInvasion(x, y, days))