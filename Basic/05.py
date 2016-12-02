'''
TASK OBJECTIVE:

Write the pseudocode corresponding to functions for addition, subtraction and
multiplication of two matrices, and then compute A=B*C –2*(B+C), where B and C are two
quadratic matrices of order n. What is the run-time?
'''

n = 5
B = [[0]*n for i in range(n)]
C = [[0]*n for i in range(n)]

B[0] = [1,2,3,4,5]
B[1] = [2,1,3,7,2]
B[2] = [5,9,1,1,4]
B[3] = [4,3,0,3,6]
B[4] = [6,4,9,8,9]

C[0] = [3,4,2,7,1]
C[1] = [1,1,7,3,2]
C[2] = [6,7,3,2,1]
C[3] = [3,2,0,1,2]
C[4] = [1,2,4,4,0]

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




