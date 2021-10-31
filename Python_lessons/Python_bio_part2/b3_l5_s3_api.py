import requests

# Программа делает api запрос на предмет интересное число или нет. Числа берем из текстового файла
with open('dataset_24476_3.txt') as file:
    # Читаем построчно
    for number in file:
        # Формируем ссылку и делаем запрос
        link = f'http://numbersapi.com/{number.strip()}/math?json=true'
        res = requests.get(link).json()
        # Выводим результат
        if res["found"] is True:
            print('Number', number.strip(), 'is Interesting')
        else:
            print('Number', number.strip(), 'is Boring')
