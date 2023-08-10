 
array = [int(x) for x in input().split(",")]
n = len(array)
present = {}
checked = {}
longest_chain = 0
for i in range(n):
    present[array[i]] = True
for i in array:
    if i not in checked and (i - 1) not in present:
        currentChain = 0
        start = i
        while start in present:
            currentChain += 1
            checked[start] = True
            start += 1
        longest_chain = max(longest_chain,currentChain)
print(longest_chain) 