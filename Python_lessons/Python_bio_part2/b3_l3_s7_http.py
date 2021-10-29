import requests
import re

# Получаем ссылку и скачиваем текст страницы
link = input()
text = requests.get(link).text
# Паттерн для выборки ссылок
pattern = r'<a.+href\=\"?\'?(?:\w+://)?(\w+(?:\.*\w+-*)+).+\"?\'?>'
# Парсим все адреса сайтов в ссылках
links = re.findall(pattern, text)
# Удаляем дубли из списка
links = list(set(links))
# Сортируем список
links.sort()
# Выводим
for element in links:
    print(element)
