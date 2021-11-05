from math import factorial

result = 0
n = int(input())
for i in range(1, n+1):
    result += factorial(i)
print(result)