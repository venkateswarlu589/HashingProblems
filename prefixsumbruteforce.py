arr = [int(x) for x in input().split()]
q = int(input())
w = int(input())
sum = 0
for i in range(q,w+1):
    sum += arr[i]
print(sum)
