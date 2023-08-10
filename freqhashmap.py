def hashmap(arr,n,quiries):
    dict = {}
    n = len(arr)
    for i in range(n):
        if arr[i] not in dict:
            dict[arr[i]] = 1
        else:
            dict[arr[i]] +=1
         
    for i in range(quiries):
        x = int(input())
        print(dict[x])
        
arr = [1,2,3,1,3,4,2]
n = len(arr)
quiries = 3
print(hashmap(arr,n,quiries))
#timecomplexity = O(N+Q)
#spacecomplexity = O(N)