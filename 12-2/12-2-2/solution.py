#imports
from functools import reduce
import string
import operator

#get input values
with open('input.txt') as f:
    content = f.readlines()
inputs = [x.strip() for x in content] 

#setup letter value tracking
vals = {}
i=0
for l in string.ascii_lowercase:
    vals[l] = i
    i+=1

mindiff = 10000000
words = []
for word in inputs:
    for other_word in inputs:
        diff = 0
        if other_word == word:
            continue
        for idx,c in enumerate(word):
            if other_word[idx] != c:
                diff += 1
        #print(diff)
        if diff < mindiff:
            mindiff = diff
            words = [word, other_word]

chars = ''
for c in words[0]:
    if c in words[1]:
        chars += c
print(mindiff)
print(words)
print(chars)



