from random import randint

print('test')

a = [1, 2, 3, 6, 7, 23, 3245, 2]
b = list(range(len(a)))
c = []
for i in range(len(a)):
    while True:
        x = randint(0, len(a))
        if x in b:
            b.remove(x)
            c.append(a[x])
            break
print('a:',a)
print('c:',c)