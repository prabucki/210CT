n = 12 # Columns
m = 10  # Rows
Exit = [7, 10]
Start = [6, 4]

M = [[0]*n for i in range(m)]

def PrintMatrix(X):
    for a in range(len(X)):
        print("[", end="")
        for b in range(len(X)):
            if X[a][b] == 0:
                print("   ", end="")
            else:
                print(X[a][b], " ", end="")
        print("]")
    return None

def FindPath(M, Start, Exit):
    path = []
    options = [Start.copy()]
    Current = Start


    while Current != Exit and len(options) > 0:

        Found = 0

        # Check directions
        if (M[Current[0] - 1][Current[1]]) == 1:  # North
            if ([Current[0] - 1, Current[1]]) not in path:
                options.append([Current[0] - 1, Current[1]])
            Found += 1
        if (M[Current[0]][Current[1] + 1]) == 1:  # East
            if ([Current[0], Current[1] + 1]) not in path:
                options.append([Current[0], Current[1] + 1])
            Found += 1
        if (M[Current[0] + 1][Current[1]]) == 1:  # South
            if ([Current[0] + 1, Current[1]]) not in path:
                options.append([Current[0] + 1, Current[1]])
            Found += 1
        if (M[Current[0]][Current[1] - 1]) == 1:  # West
            if ([Current[0], Current[1] - 1]) not in path:
                options.append([Current[0], Current[1] - 1])
            Found += 1

        # Mark dead end
        if Found == 1 and Current != Start:
            M[Current[0]][Current[1]] = 0
            Current = path[-1]
            del path[-1]
        else:
            if Current not in path:
                path.append(Current)
            Current = options[-1]
            del options[-1]
    if len(options) == 0:
        print('There is no way to exit')
    if Current == Exit:
        print('Path found! Results given in [y][x] format:')
        path.append(Current)
    print(path)


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

PrintMatrix(M)
FindPath(M, Start, Exit)