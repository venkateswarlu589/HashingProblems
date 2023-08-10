nums = [int(x) for x in input().split(",")]
n = len(nums)
if set(nums) == nums:
    print(sum(nums))
sum = 0
max_sum = 0
hashmap = {}
for i in range(n):
    sum += nums[i]
    if sum not in hashmap:
        hashmap[sum] = i
        max_sum = max(max_sum,sum)
print(hashmap[max_sum])
hashmap2 ={}
for i in range(n):
    if nums[i] not in hashmap2:
        hashmap2[nums[i]] = 1
    else:
        hashmap2[nums[i]] += 1
maxii = 0
print(type(nums))
for i in hashmap2.values():
    maxii = max(maxii,i)
if maxii == 1:
    total = 0
    for i in range(n):
        total += nums[i]
    print(total)


