import requests
import json

client_id = 'a0112a00a486e576f6be'
client_secret = 'f091aef8cff5f964181270bf8dee9e91'
link = 'https://api.artsy.net/api/tokens/xapp_token'


# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)
# достаем токен
token = j["token"]
# Программа делает api запрос
headers = {"X-Xapp-Token" : token}

result = []
with open('dataset_24476_4.txt') as file:
    # Читаем построчно
    for line in file:
        line = line.strip()
        # Формируем ссылку и делаем запрос
        res = requests.get(f'https://api.artsy.net/api/artists/{line}', headers=headers)
        res.encoding = 'utf-8'
        data = res.json()
        in_result = str(data['birthday'] + ' ' + data['sortable_name'])
        print(in_result)
        result.append(in_result)
result.sort()
for i in result:
    print(i[5:])
