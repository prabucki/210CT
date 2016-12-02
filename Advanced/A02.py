'''
TASK OBJECTIVE:

A sparse matrix is a matrix where the number of elements which are zero is bigger than the
number of elements which are not zero. Find a way to store sparse matrices, and write the
functions to add, subtract, and multiply pairs of such matrices. Do not use predefined
functions for the operations on matrices in your programming language of choice.
'''

# Variables

x = 5 # rows of matrix
y = 5 # columns of matrix
B = [[0]*x for i in range(y)] # Creates empty matrix to fill
C = [[0]*x for i in range(y)]

B[0] = [4,0,2,0,0]
B[1] = [0,0,0,0,0]
B[2] = [0,1,4,0,0]
B[3] = [3,0,0,5,0]
B[4] = [0,0,0,1,1]

C[0] = [1,0,0,0,9]
C[1] = [0,0,0,3,0]
C[2] = [0,0,0,0,0]
C[3] = [0,0,0,1,0]
C[4] = [0,0,8,0,0]


class SparseMatrix(object):
    def __init__(self, size, values):
        self.size = size
        self.values = values

def isSparse(X):
    '''Check whether given matrix is sparse - contains more zeroes than non-zeroes'''

    zero = 0
    for x in range(len(X)):
        for y in range(len(X[x])):
            if X[x][y] == 0:
                zero += 1
    if zero > (len(X) * len(X[0])) / 2:
        print('Matrix is sparse')
    else:
        print('Matrix is NOT sparse')



def Addition(X, Y):
    '''Adds both matrices to each other'''
    Z = [[0] * len(Y) for i in range(len(Y))]
    for a in range(len(X)):
        for b in range(len(X)):
            Z[a][b] = X[a][b] + Y[a][b]
    return Z

def Substraction(X, Y):
    '''Subtracts second matrix from the first one'''
    Z = [[0] * len(Y) for i in range(len(Y))]
    for a in range(len(X)):
        for b in range(len(X)):
            Z[a][b] = X[a][b] - Y[a][b]
    return Z

def Multiplication(X, Y):
    ''' Multiplies two given matrices'''
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
    '''Prints given matrix in visual form'''
    for a in range(len(X)):
        print("[ ", end="")
        for b in range(len(X)):
            print(X[a][b], " ", end="")
        print("]")
    print()
    isSparse(X)
    return None

print()
Matrix1 = SparseMatrix( [len(B), len(B[0])], B)
Matrix2 = SparseMatrix( [len(B), len(B[0])], B)
PrintMatrix(Multiplication(Matrix1.values, Matrix2.values))

