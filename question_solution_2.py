s1 = eval(input())
ls1 = {}
for i in s1:
    if s1[i] in range(0,10000):
        ls1[i] = s1[i]
    else:
        for j in s1[i]:
            if s1[i][j] in range(0,100000):
                ls1[i+'.'+j] = s1[i][j]
            else:
                for k in s1[i][j]:
                    if s1[i][j][k] in range(0,1000000):
                        ls1[i + '.' + j + '.' +k] = s1[i][j][k]
print(ls1)

