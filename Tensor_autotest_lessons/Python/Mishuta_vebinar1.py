# При заданном целом трехзначном числе n
# посчитайте n + nn + nnn
number = 123
result = number % 100 + number % 10 + number
print(result)


# Сложите цифры целого числа
# Я бы решил через цикл, так мы не привязаны к длине числа
number2 = '1234'
result2 = int(number2[0]) + int(number2[1]) + int(number2[2]) + int(number2[3])
print(result2)


# ∛343 - Найти корень третьей степени из 343
result3 = 343 ** 1/3
print(result3)


# В строке удалить все буквы "а" и подсчитать количество удаленных символов.
string4 = 'Собака, рыба, корова, кот, петух'
print(string4.count('а'))
print(string4.replace('а', ''))


# Написать произвольную анкеты, и вывести полученные данные
first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
age = input('Введите возраст: ')
sex = input('Введите пол: ')
spec = input('Введите специальность: ')
print('Имя: ', first_name)
print('Фамилия: ', last_name)
print('Специальность: ', spec)
print('Возраст: ', age)
print('Пол: ', sex)


# Проверить, что номера телефонов состоят только из цифр. Они могут начинаться с «+»,
# цифры могут быть разделены пробелами и дефисами «-»
# Например:
# 8-999-777-1111
# +7 999 333 2222
# +7 999-555-11-11
phone_number = '8-999-777-1111'
phone_number = phone_number.replace('+', '').replace(' ', '').replace('-', '')
print(phone_number.isdigit())


# Посчитать количество слов в строке
string7 = 'Съешь еще этих мягких французских булок да выпей чаю'
print(string7.count(' ') + 1)


# Дана строка, содержащая полное имя файла (например, C:\development\inside\test-project_management\inside\myfile.txt').
# Выделите из этой строки имя файла без расширения
file_path = r'C:\development\inside\test-project_management\inside\myfile.txt'
start = file_path.rfind('\\')+1     # Ищем начало имени файла
end = file_path.rfind('.')          # Ищем конец имени файла
file_name = file_path[start:end]    # Слайсом отрезаем лишнее
print(file_name)
