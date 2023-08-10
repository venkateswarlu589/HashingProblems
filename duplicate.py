list_1 = [1,2,3,4]
count = 0
for i in range(len(list_1)):
    for j in range(i + 1,len(list_1)):
        if (list_1[i] + list_1[j]) // 2 == list_1[i]:

            count += 1
if count > 0:
    print("TRUE")
else:
    print("FALSE")