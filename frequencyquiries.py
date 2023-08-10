#finding the freuency of element in an array with q quiries
def freqele(arr,n,quiries):
    n = len(arr)
    dict = {}
    list_1 = [0]*n
    for i in range(n):
        x = arr[i]
        list_1[x] +=1
    for i in range(quiries):
        i = int(input())
        print(list_1[i])
    return 0
    
arr = [8,3,5,2,3,1,6,5,7,4,3,1,4]
n = len(arr)
r = int(input())
print(freqele(arr,n,r))
#timecomplexity == O(N+Q)
#spacecomplexity == O(N)



