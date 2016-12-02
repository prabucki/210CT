'''
TASK OBJECTIVE:

Write a program to predict the number of creatures in a fictional alien invasion. An alien
lays X eggs each day (there are no genders in this species) and the eggs hatch after Y days. If
X is 3 and Y is 5, how many aliens will there be 30 days after a single alien invades?
'''

def AlienInvasion(x, y, days):
    '''
    Predicts the number of creatures in a fictional alien invasion. An alien
    lays X eggs each day (there are no genders in this species) and the eggs hatch after Y days.
    '''

    day = 1
    aliens = 1
    HatchedEggs = {} # key = days for egg to hatch, value = number of eggs

    # Fill HatchedEggs with 0s
    for i in range(y+1):
        HatchedEggs[i] = 0

    # Loop iterating over each day
    while day <= days:
        aliens += HatchedEggs[0]    # Add hatched aliens to breeding community
        HatchedEggs[y] = aliens * x # Breeding process

        # Decrease number of days for each egg to hatch
        for i in range(1, y + 1):
            HatchedEggs[i-1] = HatchedEggs[i]

        print('After day', day,': ', aliens, 'aliens, ', HatchedEggs[y], 'hatched eggs today')
        day += 1

    return aliens

# Variables
x = 3 # Eggs alien lays each day
y = 5 # Days after egg hatches
days = 30

print()
print('Final result: ',AlienInvasion(x, y, days))