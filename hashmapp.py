from collections import defaultdict
arr = [int(x) for x in input().split(",")]
length = len(arr)
dict = defaultdict(int)
for i in range(length):
    dict[arr[i]] +=1
max_freq = 0
for i in dict.items():
    if i[1] > max_freq:
        max_freq = i[1]
print(max_freq)