string = "abdadccacd"
sub_string = "edac"
hashmap = {}
for i in range(len(string)):
    if string[i] not in hashmap:
        hashmap[string[i]] = 1
    else:
        hashmap[string[i]] += 1
for i in sub_string:
    if i in hashmap:
        print(hashmap[i])
        break
    else:
        print("0")
        break