def maxdistance(arr):
    n = len(arr)
    max_dis = 0
    hashmap = {}
    for i in range(n):
        if arr[i] not in hashmap:
            hashmap[arr[i]] = i
        else:
            distance = i - hashmap[arr[i]]
            max_dis = max(distance,max_dis)
    
    return max_dis
arr = [1,1,2,2,3,1]
print(maxdistance(arr))
#take the hashmap and insert the key value pairs as elements and its index occurrences.then if the element occurs in hashmap then subtract the last occurrence of
#index of last occurence and index of first occurrence .declare it as max distance and update it.