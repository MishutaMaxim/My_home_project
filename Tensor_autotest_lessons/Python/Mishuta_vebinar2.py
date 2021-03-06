# Задание 1: Вывести на экран все чётные, кратные трём, значения в диапазоне от 1 до 123
for i in range(1, 124):             # Запускаем цикл 1-123
    if i % 2 == 0 and i % 3 == 0:   # Проверяем условие кратности 2 и 3
        print(i, end=' ')           # Печатаем значение без перевода строки
print()


# Задание 2: Вывести на экран циклом N строк из * где каждая строка пронумерована и длинна равна номеру
number_of_lines = int(input('Введите число строк N: '))     # Получаем число строк
for i in range(1, number_of_lines + 1):     # Запускаем цикл от 1 до N+1
    print(i, '*' * i)   # Печатаем число и *
print()


# Задание 3: Посчитать двойной факториал числа N
number = int(input('Введите число N: '))    # Получаем число N
result = 1                                  # Объявляем переменную с результатом
while number > 0:                           # Запускаем цикл
    result *= number                        # Получаем произведение всех чисел на N
    number -= 2                             # Уменьшаем N на 2
print('Результат: ', result)                # Выводим результат
print()


# Задание 4: Для каждого числа от 1 до 100, вывести список чисел меньше текущего и кратного 5.
# Например: 11 – [5, 10], 44 – [0, 5, 10, 15, 20, 25, 30, 35, 40]
for i in range(1, 101):             # Запускаем цикл на отрезке
    result = []                     # Объявляем пустой список для i
    for j in range(1, i):           # Запускаем цикл для чисел меньше i
        if j % 5 == 0:              # Если число кратно 5
            result.append(j)        # Добавляем в список
    print(i, result)                # Выводим i и список чисел удовлетворяющих условию
print()


# Задание 5: Поменять местами самый большой и самый маленький элементы списка
list5 = [5, 10, 0, 15, 20, 25, 30, 40, 35]
print('Исходный список:', list5)
min_number = min(list5)
min_index = list5.index(min_number)
max_number = max(list5)
max_index = list5.index(max_number)
list5[min_index], list5[max_index] = max_number, min_number
print('Новый список:', list5)
print()


# Задание 6: Найдите сумму и произведение элементов списка. Результаты вывести на экран
list6 = [1, 2, 100]
print('Список: ', list6)
summ = 0
proz = 1
for element in list6:   # Тут довольно просто, перебираем все элементы и добавляем элементы к сумме и произведению
    summ += element
    proz *= element
print('Сумма элементов списка = ', summ)
print('Произведение элементов списка = ', summ)
print()


# Задание 7: Дан список словарей:
# [{“наименование”: “Спички”, “цена”: 1},
#  {“наименование”: “Лук”, “цена”: 37},
#  …
#  {“наименование”: str, “цена”: int}]
# Найти ТОП-2 самых дорогих товаров и вывести в том же формате.
price = [{'наименование': 'Спички', 'цена': 1},
         {'наименование': 'Сигареты', 'цена': 189},
         {'наименование': 'Лук', 'цена': 37},
         {'наименование': 'Молоко', 'цена': 58},
         {'наименование': 'Колбаса', 'цена': 105}]
top1 = price[0]
top2 = price[0]
# Циклом перебираем все элементы в прайсе
for product in price:
    # Если цена элемента больше цены топ1, то сдвигаем топ2 и записываем новый топ1
    if product['цена'] > top1['цена']:
        top2 = top1
        top1 = product
    # Если цена элемента больше цены топ2, то записываем новый топ2
    elif product['цена'] > top2['цена']:
        top2 = product
print(top1)
print(top2)
