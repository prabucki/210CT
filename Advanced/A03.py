'''
TASK OBJECTIVE:

Given two strings of n and m integer elements, write the pseudocode to compute:
a) The string that contains all the elements belonging to both strings.
b) The string of all the elements of the two given strings, written once.
c) The string of the elements from the first string, without the elements that are also in the
second string.
What's the run time?
'''

from random import randint

def similarities(n1, n2):
    found = []
    for a in n1:
        for b in n2:
            if a==b and a not in found:
                found.append(a)
    return found

def everything(n1, n2):
    found = []
    for a in n1:
        if a not in found:
            found.append(a)
    for b in n2:
        if b not in found:
            found.append(b)
    return found

def FirstStringOnly(n1, n2):
    for b in n2:
        for a in n1:
            if b==a:
                n1.remove(a)
    return n1



n = 10
m = 5
numbers = [[], []]
z = [n, m]

for i in range(n):
    numbers[0].append(randint(1, 20))
for i in range(m):
    numbers[1].append(randint(1, 20))

print(numbers[0])
print(numbers[1])
print('Similarities: ',similarities(numbers[0], numbers[1]))
print('Everything: ', everything(numbers[0], numbers[1]))
print('First String Only: ', FirstStringOnly(numbers[0], numbers[1]))