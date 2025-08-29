phrase = 'less is more'
vowels = set(['a','e','i','o','u'])
count = 0
for vowel in phrase:
    if vowel in vowels:
        count+=1
print(count)