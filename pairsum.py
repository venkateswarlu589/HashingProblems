def pairsum(arr,target):
    n = len(arr)
    hashmap = {}
    for i in range(n):
        diff = target - arr[i]
        if diff in hashmap:
            list_1 = []
            list_1.append(hashmap[diff])
            list_1.append(i)
            return list_1
        hashmap[arr[i]] = i
arr = [1,3,6,2,7,4]
target = 11
print(pairsum(arr,target))