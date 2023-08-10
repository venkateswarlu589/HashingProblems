def prefixsum(arr):
    n = len(arr)
    m = n + 1
    prefix_sum = [0]*n
    for i in range(1,len(prefix_sum)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    return prefix_sum
arr = [1,2,3,4,5,6,7,8,9]
prefix_sum =[0,0,0,0,0,0,0,0,0]
print(prefixsum(arr))