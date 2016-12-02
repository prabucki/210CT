a = 4617
b = 5
power=1
result=0

while b<=a:
    b = b * 5
    power+=1

for i in range(power):
    result+=int(a/(5**(i+1)))

print(result)