nums = [int(x) for x in input().split(",")]
hashmap = {}
stack  = []
for i in range(len(nums)):
    if nums[i] not in hashmap:
        hashmap[nums[i]] = 1
    else:
        hashmap[nums[i]] += 1
for i in range(1,len(nums)):
    if i not in hashmap:
        stack.append(i)
print(stack)