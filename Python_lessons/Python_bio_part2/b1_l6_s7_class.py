class graph(dict):
    def __init__(self):
        self.clas = {}
        print('инициировали словарь классов')
        #создаем пустой словарь при обращении к графу классов

    def add_element(self, parent, baby):
        print('пытаемся добавить детей ', baby, ' для предка ', parent)

    def chek_element(self, predok, potomok):
        print('пытаемся проверить ребенка ', baby, ' для предка ', parent)

x = graph()
for i in range(int(input())):
    parent, baby = input().split(' : ')
    x.add_element(parent, baby.split())