#minimum operattions to required to make the array equal
arr = [int(x) for x in input().split(",")]
dict = {}
for i in range(len(arr)):
    x = arr[i]
    if x not in dict:
        dict[arr[i]] = 1
    else:
        dict[arr[i]] += 1

for i in dict.values():
    y = 0
    y = max(i,y)

print(len(arr)-y)
