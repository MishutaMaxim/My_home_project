import requests
import re
""""
Парсер смотрит можно ли из первой ссылки попасть на вторую ровно через 1 переход.
"""

#Получаем ссылки
link1 = input()
link2 = input()
flag = 0
# Парсим ссылки с первой страницы и упаковываем в лист
text1 = requests.get(link1).text
links = re.findall(r'https:.+?html', text1)
# Поочередно переходим по ссылкам из списка и ищем там конечную ссылку, если находим
# то обрываем цикл и выводим Да
for link in links:
    text2 = requests.get(link).text
    result = re.findall(r'https:.+?html', text2)
    if link2 in result:
        print('Yes')
        flag = 1
        break

# Если в цикле мы не нашли ссылку - выводим Нет
if flag == 0:
    print('No')
