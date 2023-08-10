nums = [1,2,3,4,1,3,2,6,8]
hashmap = {}
matrix = []
for i in range(len(nums)):
    if nums[i] not in hashmap:
        hashmap[nums[i]] = 1
    else:
        hashmap[nums[i]] += 1

for i in range(len(nums)):
    ans  = []
    if nums[i] not in ans:
        ans.append(nums[i])
        matrix.append(ans)
    
    
    
        
        
        
        
print(ans)

