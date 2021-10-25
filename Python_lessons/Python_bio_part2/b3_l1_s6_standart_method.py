s = input()
a = input()
b = input()
counter = 0
for i in range(1001):
    if a in s and a in b:
        print('Impossible')
        break
    elif a in s:
        s = s.replace(a, b)
        counter += 1
    else:
        print(counter)
        break