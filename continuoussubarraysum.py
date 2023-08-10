array = [1,4,7,2,4,3,8,6]
k = 6
prefix_sum = 0
hashmap = {}
for i in range(len(array)):
    prefix_sum += array[i]
    prefix_sum_mode = prefix_sum % k
    if prefix_sum_mode == 0 and i + 1 >= 2:
        print("VALID")
    if prefix_sum_mode in hashmap:
        if i - hashmap[prefix_sum_mode] >= 2:
            print("VALID")
    else:
        hashmap[prefix_sum_mode] = i
