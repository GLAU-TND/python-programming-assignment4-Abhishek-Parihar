l1 = eval(input())
k = ''
n = -1
ls1 = eval(str([[]]*26))
for i in range(len(l1)):
    if l1[i][0] != k:
        k = l1[i][0]
        n += 1
    if l1[i][0] == k:
        ls1[n].append(l1[i][1])
for i in range(len(ls1)):
    if [] in ls1:
        ls1.remove(ls1[-1])
l = 1000
k1 = 0
k2 = 0
for i in range(len(ls1)):
    for j in range(len(ls1)):
        if i != j and j>i:
            a1 = set(ls1[i])
            a2 = set(ls1[j])
            m = a1 if len(a1)>len(a2) else a2
            if a1.union(a2) == m:
                if abs(len(a1)-len(a2))<l:
                    l = abs(len(a1)-len(a2))
                    k1 = 97+i
                    k2 = 97+j
print(chr(k1),chr(k2))