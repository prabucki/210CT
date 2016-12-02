from math import sqrt
a = 12131423

for i in range(a,0,-1):
    if sqrt(i).is_integer():
        print(i)
        break
