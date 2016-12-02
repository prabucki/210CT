#I assume I can't use text.split()

a = 'This is awesome'
word = ''
result = ''

for i in range(len(a)):
    if a[i] !=' ':
        word+=a[i]
    else:
        result=word+' '+result
        word=''

result = word + ' ' + result
print(result)
