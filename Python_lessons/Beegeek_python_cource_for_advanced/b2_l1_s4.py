"""
Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ
(в том числе пробел) стоит 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.
"""


def string_price(string: str):
    result = len(string) * 60
    output = str(result // 100) + ' р. ' + str(result % 100) + ' коп.'
    return output


some_string = input()
print(string_price(some_string))
