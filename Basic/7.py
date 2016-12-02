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