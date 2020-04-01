s1 = input()
s2 = eval(input())
l1 = []
for i in s2:
    if i.startswith(s1):
        l1.append(i)
print(l1)
