def sol(v):
    sum = 0
    while v != 0:
        sum = sum + v % 10
        v = v // 10
    return sum
 
n = int(input())
b = [0] * (n + 1)
 
i = 1
while i <= n:
    b[i] = int(input())
    i += 1
 
kk = {}
i = 1
answer = -1
 
while i <= n:
    if sol(b[i]) in kk:
        pp = b[i] + kk[sol(b[i])]
        answer = max(answer, pp)
        kk[sol(b[i])] = max(kk[sol(b[i])], b[i])
    else:
        kk[sol(b[i])] = b[i]
    i += 1
 
print(answer)