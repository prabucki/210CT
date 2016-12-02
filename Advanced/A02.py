'''
TASK OBJECTIVE:

A sparse matrix is a matrix where the number of elements which are zero is bigger than the
number of elements which are not zero. Find a way to store sparse matrices, and write the
functions to add, subtract, and multiply pairs of such matrices. Do not use predefined
functions for the operations on matrices in your programming language of choice.
'''

n = 5
B = [[0]*n for i in range(n)]
B = [[0]*n for i in range(n)]

# Limits =
Limits = []
Limits.append([B, n**2, 0])
Limits.append([C, n**2, 0])

B[0] = [0,0,0,0,0]
B[1] = [0,0,0,0,0]
B[2] = [0,0,0,0,0]
B[3] = [0,0,0,0,0]
B[4] = [0,0,0,0,0]

C[0] = [0,0,0,0,0]
C[1] = [0,0,0,0,0]
C[2] = [0,0,0,0,0]
C[3] = [0,0,0,0,0]
C[4] = [0,0,0,0,0]

def Addition(X, Y):
    Z = [[0] * len(Y) for i in range(len(Y))]
    for a in range(len(X)):
        for b in range(len(X)):
            Z[a][b] = X[a][b] + Y[a][b]
    return Z

def Substraction(X, Y):
    Z = [[0] * len(Y) for i in range(len(Y))]
    for a in range(len(X)):
        for b in range(len(X)):
            Z[a][b] = X[a][b] - Y[a][b]
    return Z

def Multiplication(X, Y):
    Z = [[0] * len(X) for i in range(len(X))]
    if type(Y) == int:
        for a in range(len(X)):
            for b in range(len(X)):
                Z[a][b] = X[a][b] * Y
    else:
        for a in range(len(X)):
            for b in range(len(X)):
                for c in range(len(X)):
                    Z[a][b] += X[a][c] * Y[c][b]
    return Z

def PrintMatrix(X):
    for a in range(len(X)):
        print("[ ", end="")
        for b in range(len(X)):
            print(X[a][b], " ", end="")
        print("]")
    return None

PrintMatrix(Substraction(Multiplication(B, C), Multiplication(Addition(B, C), 2)))




