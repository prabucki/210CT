'''
TASK OBJECTIVE:

Consider having n cubes, each being characterized by their edge length and their colour.
Use the cubes (not necessarily all of them) in order to build a tower of maximum height,
under the following conditions:
 a) any two neighbouring cubes must be of different colours.
 b) the edge length of a cube is lower than the edge length of the cube placed below it.
'''

from random import randint

# Variables
colours = {1: 'blue', 2: 'green', 3: 'red', 4: 'cyan', 5: 'magenta', 6: 'yellow', 7: 'black', 8: 'white'}
MaxLength = 30 # Maximum length of cube edge
n = 10 # Number of cubes generated
MaxHeight = 0 # Highest configuration height achieved so far
HighestTower = () # Highest configuration achieved so far

def Tower(n, MaxLength):

    # Start variables
    cubes = []
    tower = [(float('inf'), "nothing")] # "floor" of tower; doesn't have colour and is infinite
    height = 0 # Current height of tower

    # Generating cubes
    for i in range(n):
        colour = randint(1, len(colours)) # Assign random colour from dictionary
        length = randint(1, MaxLength)  # Assign random edge length
        cubes.append((length, colours[colour]))
    print("Available cubes: ", cubes)

    Bruteforce(cubes, height, tower)

def Bruteforce(cubes, height, tower):
    '''
    Recursive function that tries every possible combination of cubes, to look for highest one.
    '''

    global MaxHeight
    global HighestTower


    for i in range(len(cubes)): # Try every cube left in stock

        if (cubes[i][1] != tower[-1][1]) and (cubes[i][0] < tower[-1][0]): # Check if current cube meets criteria
            height += cubes[i][0] # Increase current height by new cube length
            tower.append(cubes[i]) # Add cube to current configuration
            cubes.pop(i)    # Remove cube from available stock

            if height > MaxHeight:  # Check if new configuration is highest one so far
                MaxHeight = height
                HighestTower = tower.copy()

            # Look for next cubes to add to current configuration
            Bruteforce(cubes, height, tower)

            # Remove cube from tower and put back to available stock
            cubes.append(tower[-1])
            height -= tower[-1][0]
            tower.pop(-1)

print()
Tower(n, MaxLength)

print("Highest Tower: ", HighestTower[1:])
print('Height: ',MaxHeight)