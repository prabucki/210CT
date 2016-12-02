'''
TASK OBJECTIVE:

Write a recursive function (pseudocode and code) that removes all vowels from a given
string s. Input: "beautiful" Output: "btfl".
'''

vowels="aeiou"
a = "beautiful"

def unVowel(x):
    for i in range(len(x)):
        for j in vowels:
            if x[i]==j:
                return unVowel(x[:i] + x[i+1:])
    return x


print(unVowel(a))
