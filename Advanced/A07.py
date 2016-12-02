'''
TASK OBJECTIVE:

Let's consider a labyrinth as a n × m matrix, where the corridors are denoted by 1s situated
in consecutive positions on the same line or column. The rest of the elements are 0. Within
the labyrinth, a person is considered to be in position (i, j). Write a program that lists all exit
routes which do not pass the same place twice.
Input: n, m, the rows of the matrix, the coordinates of the exit and the coordinates of the
person (row, column). Output: a sequence of row/column pairs representing the person's
successive position.
'''

# Variables
n = 12 # Columns
m = 10  # Rows
Exit = [7, 10]
Start = [6, 4]

M = [[0]*n for i in range(m)]   # Creates empty matrix of given size

# Generate matrix (1s are corridors, 0s are walls)
M[0] = [0,0,0,0,0,0,0,0,0,0,0,0]
M[1] = [0,1,0,1,0,1,1,1,1,1,0,0]
M[2] = [0,1,1,1,1,1,0,0,0,1,1,0]
M[3] = [0,0,0,0,1,1,0,1,1,1,0,0]
M[4] = [0,1,1,0,1,1,1,0,1,0,1,0]
M[5] = [0,0,1,0,0,0,0,0,1,1,1,0]
M[6] = [0,0,1,0,1,0,1,1,1,0,0,0]
M[7] = [0,1,1,1,1,0,0,1,0,0,1,0]
M[8] = [0,1,0,0,1,1,1,1,1,1,1,0]
M[9] = [0,0,0,0,0,0,0,0,0,0,0,0]


def FindPath(M, Start, Exit):
    '''Finds the path of adjacent 1s in given matrix, from Start field to Exit field'''

    # Start Variables
    path = []   #
    options = [Start.copy()] # Discovered ways
    Current = Start

    while Current != Exit and len(options) > 0:

        Found = 0 # Number of ways found from current location (including return)

        # Look for available ways from current position and add them to available ways

        # Check North
        if (M[Current[0] - 1][Current[1]]) == 1:
            if ([Current[0] - 1, Current[1]]) not in path:
                options.append([Current[0] - 1, Current[1]])
            Found += 1

        # Check East
        if (M[Current[0]][Current[1] + 1]) == 1:
            if ([Current[0], Current[1] + 1]) not in path:
                options.append([Current[0], Current[1] + 1])
            Found += 1

        # Check South
        if (M[Current[0] + 1][Current[1]]) == 1:
            if ([Current[0] + 1, Current[1]]) not in path:
                options.append([Current[0] + 1, Current[1]])
            Found += 1

        # Check West
        if (M[Current[0]][Current[1] - 1]) == 1:
            if ([Current[0], Current[1] - 1]) not in path:
                options.append([Current[0], Current[1] - 1])
            Found += 1

        # Mark Dead End
        if Found == 1 and Current != Start: # check if only one way was found (return one)
            M[Current[0]][Current[1]] = 0 # Mark corridor as wall in the matrix
            Current = path[-1] # Go back from where you came
            del path[-1]
        else:
            if Current not in path: # We haven't been here yet
                path.append(Current)    # Add location to our path
            Current = options[-1]   # Remove current location from available ways
            del options[-1]

    # Check if we have run out of options:
    if len(options) == 0:
        print('There is no way to exit')

    # Check if you have reached the Exit
    if Current == Exit:
        print('Path found! Results given in [y][x] format:')
        path.append(Current)
    return path


def PrintMatrix(X):
    '''Prints given matrix in a simple visual form'''

    for a in range(len(X)):
        print("[ ", end="")
        for b in range(len(X[0])):
            if a == Exit[0] and b == Exit[1]:
                print('E  ', end="")
            elif a == Start[0] and b == Start[1]:
                print("S  ", end="")
            elif X[a][b] == 0:
                print("   ", end="")
            else:
                print(X[a][b], " ", end="")
        print("]")

print()
PrintMatrix(M)
print()
print(FindPath(M, Start, Exit))