array = [int(x) for x in input().split(",")]
n= len(array)
sum = 0
max_length =0
hashmap = {}
for i in range(n):
    sum += array[i]
    if sum == 0:
        max_length = i + 1
    elif sum in hashmap:
        max_length = max(max_length,i-hashmap[sum])
    else:
        hashmap[sum] = i
print(max_length)

