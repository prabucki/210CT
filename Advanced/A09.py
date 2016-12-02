'''
TASK OBJECTIVE:

. Write a function to calculate the kth power of a square matrix, using pointers to access to
the elements of the matrix. The resulted matrix will be displayed in natural form.
'''

# Variables
n = 5
k = 3

# Generate empty square matrix of size n
B = [[0]*n for i in range(n)]

# Populate matrix with numbers
B[0] = [1,2,3,4,5]
B[1] = [2,1,3,7,2]
B[2] = [5,9,1,1,4]
B[3] = [4,3,0,3,6]
B[4] = [6,4,9,8,9]

def Multiplication(X, power):
    '''Multiplicates given matrix to given power'''

    Multiplier = X

    for i in range(power-1):
        Result = [[0] * len(X) for i in range(len(X))] # creates empty matrix to store result in
        for a in range(len(X)):
            for b in range(len(X)):
                for c in range(len(X)):
                    Result[a][b] += Multiplier[a][c] * X[c][b]
        Multiplier = Result

    return Multiplier

def PrintMatrix(X):
    ''' Displays matrix in natural form'''
    for a in range(len(X)):
        print("[ ", end="")
        for b in range(len(X)):
            print(X[a][b], " ", end="")
        print("]")

print()
print('Matrix B to power of: ', k)
print()
PrintMatrix(Multiplication(B, k))
print()