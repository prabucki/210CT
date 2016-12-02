'''
TASK OBJECTIVE:

Given a sequence of n integer numbers, extract the sub-sequence of maximum length
which is in ascending order.
'''

# Note: remove scores with len(L2/L3) later on

n = 11
L = [5, 123, 34, 12, 68, 1, 95, 100, 2, 2, 3, 4, 5, 3]

def AscendingSubsequence(L):
    L3 = []
    L2 = [L[1]]
    score = 1
    topscore = 0
    for i in range(len(L)-1):
        if L[i]<=L[i+1]:
            L2.append(L[i+1])
            score+=1
            if score > topscore:
                topscore = score
                L3=L2
        else:
            score=1
            L2=[L[i+1]]
    return(L3)

print(AscendingSubsequence(L))