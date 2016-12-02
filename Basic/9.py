L = [2, 3, 5, 7, 9, 13]
low = 10
high = 14

def binarySearch(L, low, high):
    first = 0
    last = len(L)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if L[midpoint] >= low and L[midpoint] <= high:
            found = True
        else:
            if high < L[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

print(binarySearch(L, low, high))