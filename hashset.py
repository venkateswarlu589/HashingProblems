ar = [8,4,7,2,8]
count = 0
ar1 = [7,2,8,10]
b = set()
for i in range(len(ar)):
    b.add(ar[i])
for j in range(len(ar1)):
    if ar1[j] not  in b:
        print("It is a not a subset")
        exit()
print("Subset")