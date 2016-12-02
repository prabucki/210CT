'''
TASK OBJECTIVE:

Write a recursive function (pseudocode and code) to check if a number n is prime (hint:
check whether n is divisible by any number below n).
'''


n=6

def isPrimeRecursive(x):
    global n
    if x==1:
        return True
    elif n%x==0 and n!=x:
        return False
    else:
        return isPrimeRecursive(x-1)

print(isPrimeRecursive(n))