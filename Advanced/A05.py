'''
TASK OBJECTIVE:

In addition to the normal homework task, write a function that takes four parameters
representing the constant and multiplier of two linearly growing (as in O(m × n + k) )
functions and determines the critical value of n (which should be an integer) at which the
relative run-time of the two algorithms switches. That is, at which input size is algorithm A
slower than B and at which is B slower than A? Use an iterative approach rather than
solving the equations.
'''

# Functions pattern: O(m × n + k)

# Variables
multiplier1 = 6
constant1 = 21

multiplier2 = 3
constant2 = 134

def CompareBigO(c1, c2, m1, m2):
    '''Function compares run-time of 2 given functions and returns integer "n" when they intercept'''

    n = 0
    o1 = m1 * n + c1
    o2 = m2 * n + c2

    # Check for similarities
    if m1 == m2: # Functions are parallel and will not intercept
        if c1 == c2:
            return(print("n = ",0, '(Functions are identical)'))
        return(print("n = ",None, '(Constants are different, functions will never intercept)'))
    if (m1 > m2 and c2 > c2) or (m1 < m2 and c1 < c2):
        return(print("n = ",None, '(Both constant and multiplier are bigger in one function, functions will never intercept)'))

    while True:

        Before = o2 > o1
        o1 = m1 * n + c1
        o2 = m2 * n + c2
        After = o2 > o1

        # Check if one function exceeded the other one
        if Before != After:
            return(print('n = ',n))

        n += 1

print()
CompareBigO( constant1, constant2, multiplier1, multiplier2)