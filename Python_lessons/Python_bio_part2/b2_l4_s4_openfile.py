temp = []

# Читаем файл в список
with open('dataset_24465_4.txt') as file:
    for line in file:
        temp.append(line)

# Инвертируем список
temp.reverse()

# Записываем в файл
with open('result.txt', 'w') as result:
    for i in temp:
        result.write(i)

print('Я закончил')