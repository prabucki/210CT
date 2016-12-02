'''
TASK OBJECTIVE:

Adapt the quick sort algorithm to find the mth smallest element out of a sequence of n
integers.
'''

from random import randint



def QuickSort(numbers, m):


    if len(numbers) < m:
        return ('No such number')
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
        if len(smaller) < m and len(smaller)+len(equal)>=m:
            return equal[0]

n = 10
m = 3

numbers = []
for i in range(n):
    numbers.append(randint(1, 20))
print('Numbers: ', numbers)

print(m,'smallest number: ',QuickSort(numbers, m))