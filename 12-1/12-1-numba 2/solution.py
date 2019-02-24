import time
from functools import reduce
with open('input.txt') as f:
    content = f.readlines()
nums = [int(x.strip()) for x in content] 

list_sums = {"0": True}
sum = 0

go = True
x = 0
start = time.time()
while go:
    if x == len(nums):
        x = 0
    sum += nums[x]
    #print(sum)

    if sum in list_sums:
        #print(list_sums)
        print(sum)
        go = False
    else:
        list_sums[sum]=True
        x += 1
end = time.time()
print(end-start)