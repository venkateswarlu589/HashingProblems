#checking the frequency of element in an array
#creating an empty dictionary
#set the frequency of each elemnt in empty dictonary
ar = [1,3,3,4,5,4,4,4,4]
length = len(ar)
dict = {}
for i in range(length):
    x = ar[i]
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1
q = [3,4,1]
for i in range(len(q)):
    print(dict[q[i]],end= " ")


