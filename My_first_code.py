with open('dataset_3363_2 (2).txt') as inf:
    s = inf.readline().lower().strip()
result = ''
n = ''
buk=''
for i in range(len(s)):
    if s[i].isalpha():
        buk = s[i]
    elif s[i].isdigit():
        n += s[i]
        if i==len(s)-1 or s[i+1].isalpha():
            result += buk*(int(n))
            n = ''
print(result)
with open('result.txt','w') as ouf:
    ouf.write(str(result))