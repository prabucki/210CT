'''
TASK OBJECTIVE:

Adapt the quick sort algorithm to find the mth smallest element out of a sequence of n
integers.
'''

from random import randint

# Variables
n = 10
m = 3

def QuickSort(numbers, m):
    ''' Modified QuickSort function, that instead of sorting the list looks for mth smallest element'''

    if len(numbers) < m: # Check if m exceeds list elements
        return ('No such number')

    # Start Quick Sort
    for i in range(len(numbers)):
        smaller = []
        equal = []
        bigger = []
        pivot = numbers[i]
        for n in numbers:
            if n > pivot:
                bigger.append(n)
            elif n == pivot:
                equal.append(n)
            else:
                smaller.append(n)
        # Check if Equal sequence contains mth element of list
        if len(smaller) < m and len(smaller)+len(equal)>=m:
            return equal[0] # Since all elements in equal list are the same, we can return any element

# Generate random list of numbers from 1 to 20 of n size
numbers = []
for i in range(n):
    numbers.append(randint(1, 20))

print()
print('Generated numbers: ', numbers)
print(m,'th smallest number: ',QuickSort(numbers, m))