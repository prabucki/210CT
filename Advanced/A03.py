'''
TASK OBJECTIVE:

Given two strings of n and m integer elements, write the pseudocode to compute:
a) The string that contains all the elements belonging to both strings.
b) The string of all the elements of the two given strings, written once.
c) The string of the elements from the first string, without the elements that are also in the
second string.
What's the run time?
'''

'''
------PSEUDO CODE------

EVERYTHING(A,B)
	string FOUND
	FOR i <- 1 to LENGTH(A)
		FOUND[i] <- A[i]
	FOR j <- 1 to LENGTH(B)
		FOUND[i+j] <- B[j]
	RETURN FOUND

Run Time:  O(n)

EVERYTHING_ONCE(A,B)
	string FOUND
	FOR a <- 1 to LENGTH(A)
	    IF a NOT IN FOUND
	        FOUND.append(A[i])
		FOR b <- 1 to LENGTH(B)
			IF b NOT IN FOUND
				FOUND.append(B[i])
	RETURN FOUND

Run Time: O(n^2)

FIRST_STRING_ONLY (A,B)
	FOR a <- 1 to LENGTH(A)
		FOR b <- 1 to LENGTH(B)
			IF A[a] = B[b]
				A.remove(A[a])
	RETURN A

Run Time:  O(n^2)

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

# Variables
n = 10
m = 5
numbers = [[], []]
z = [n, m]

# Generating 2 lists of random numbers from 1 to 20
for i in range(n):
    numbers[0].append(randint(1, 20))
for i in range(m):
    numbers[1].append(randint(1, 20))

# Results
print(numbers[0])
print(numbers[1])
print('Similarities: ',similarities(numbers[0], numbers[1]))
print('Everything: ', everything(numbers[0], numbers[1]))
print('First String Only: ', FirstStringOnly(numbers[0], numbers[1]))