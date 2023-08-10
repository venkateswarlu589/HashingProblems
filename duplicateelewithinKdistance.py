#find duplicate elements are with in th k distance range
arr = [int(x) for x in input().split(",")]
length = len(arr)
k = int(input())
dict ={}
for i in range(length):
    if arr[i] in dict:
        dict[arr[i]] = i
    elif i-dict[arr[i]] <= k:
        print("TRUE")
    dict[arr[i]] = i
    exit()
print("FALSe")

        

    