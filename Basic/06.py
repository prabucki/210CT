'''
TASK OBJECTIVE:

Write the pseudocode and code for a function that reverses the words in a sentence. Input:
"This is awesome" Output: "awesome is This". Give the Big O notation.
'''

# Note: I assume I can't use text.split(). Task would be much easier with it

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
