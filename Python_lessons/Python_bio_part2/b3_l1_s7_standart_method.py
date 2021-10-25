s = input()
t = input()
counter = 0
start = 0

while s.find(t, start) != -1:
    counter += 1
    start = s.find(t, start) + 1
print(counter)
