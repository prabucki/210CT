'''
TASK OBJECTIVE:

Write the pseudocode for a function which returns the highest perfect square which is less
or equal to its parameter (a positive integer). Implement this in a programming language of
your choice.
'''

from math import sqrt
a = 12131423

for i in range(a,0,-1):
    if sqrt(i).is_integer():
        print(i)
        break
