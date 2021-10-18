x = input()
y = input()
s1 = {key:value for key,value in zip(list(x),list(y))}
s2 = {key:value for key,value in zip(list(y),list(x))}
a = input()
b = input()
a1 = ''
b1 = ''
for i in range(len(a)):
    a1 += s1[a[i]]
print(a1)
for i in range(len(b)):
    b1 += s2[b[i]]
print(b1)