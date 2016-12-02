from random import randint

colours = {1: 'blue', 2: 'green', 3: 'red', 4: 'cyan', 5: 'magenta', 6: 'yellow', 7: 'black', 8: 'white'}
MaxLength = 30 # Maximum length of cube edge
n = 10 # Number of cubes generated
MaxHeight = 0
HighestTower = ()

def Tower(n, MaxLength):

    global HighestTower

    # generating cubes
    cubes = []
    tower = [(float('inf'), "nothing")]
    height = 0
    for i in range(n):
        colour = randint(1, len(colours))
        length = randint(1, MaxLength)
        cubes.append((length, colours[colour]))
    print("Available: ", cubes)

    Bruteforce(cubes, height, tower)

def Bruteforce(cubes, height, tower):

    global MaxHeight
    global HighestTower

    for i in range(len(cubes)):
        if (cubes[i][1] != tower[-1][1]) and (cubes[i][0] < tower[-1][0]):
            height += cubes[i][0]
            tower.append(cubes[i])
            cubes.pop(i)

            if height > MaxHeight:
                MaxHeight = height
                HighestTower = tower.copy()

            Bruteforce(cubes, height, tower)

            # putting cube back to stock
            cubes.append(tower[-1])
            height -= tower[-1][0]
            tower.pop(-1)


Tower(n, MaxLength)
print("Highest Tower: ", HighestTower[1:])
print('Height: ',MaxHeight)