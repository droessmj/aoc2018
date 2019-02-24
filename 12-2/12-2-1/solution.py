from functools import reduce
with open('input.txt') as f:
    content = f.readlines()

inputs = [x.strip() for x in content] 

#keep totals for 2's, 3's
twos = 0
threes = 0

#foreach input, does it contain 2, does it contain 3? 
for line in inputs:
    chars = line
    two = False
    three = False
    for char in chars:
        if line.count(char) == 2:
            two = True
        if line.count(char) == 3:
            three = True
    if two:
        twos += 1
    if three:
        threes += 1

#multiply totals. print result
print(twos*threes)