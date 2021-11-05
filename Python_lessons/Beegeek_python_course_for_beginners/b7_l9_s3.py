a, b = int(input()), int(input())
max_delitel = 1
number = 0
for i in range(a, b+1):
    delitel = 0
    for j in range(1, i+1):
        if i % j == 0:
            delitel += j
    if delitel >= max_delitel:
        number = i
        max_delitel = delitel
print(number, max_delitel)
