vowels="aeiou"
a = "beautiful"

def unVowel(x):
    for i in range(len(x)):
        for j in vowels:
            if x[i]==j:
                return unVowel(x[:i] + x[i+1:])
    return x


print(unVowel(a))
