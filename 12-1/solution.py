from functools import reduce
with open('input.txt') as f:
    content = f.readlines()
nums = [x.strip() for x in content] 
nums_int = [int(x) for x in nums]
print(nums)
sum = reduce(lambda x, y: x+y, nums_int)
print(sum)