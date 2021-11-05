from math import factorial
a, b = int(input()), int(input())

for i in range(a, b+1):
    if (factorial(i - 1) + 1) % i == 0 and i > 1:
        print(i)