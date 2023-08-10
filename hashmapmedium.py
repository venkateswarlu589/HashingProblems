def hashmap(arr1,arr2,n1,n2):#checking the array is subset of another array with exist of duplicate elements
    dict = {}
    for i in range(n1):
        x = arr1[i]
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    for i in range(n2):
        if arr2[i] not in dict or dict[arr2[i]] == 0:
            return False
        dict[arr2[i]] -= 1
    return True
arr1 = [2,3,4,7,8,2,4]
arr2 = [2,4,3,7,10]
y = hashmap(arr1,arr2,len(arr1),len(arr2))
if y:
    print("Array2 is subset of arrar1")
else:
    print("not a subset")
    
