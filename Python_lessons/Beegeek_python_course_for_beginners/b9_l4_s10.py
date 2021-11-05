s = input()
max = 0
for symbol in s:
    if s.count(symbol) >= max:
        max_symbol = symbol
        max = s.count(symbol)
print(max_symbol)
