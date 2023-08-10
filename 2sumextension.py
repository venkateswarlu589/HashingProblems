def twosum(arr,k):
    n = len(arr)
    hashmap = {}
    sum = 0
    for i in range(n):
        diff = k - arr[i]
        if diff in hashmap:
            hashmap[arr[i]] = +1
            sum = max(sum,i - hashmap[arr[i]])
        else: 
            hashmap[arr[i]] = 1
            

            
    return sum
arr = [5,3,5,7,4,2,4,8,5]
k = 12
print(twosum(arr,k))
            