import csv
import collections

'''
Программа кушает csv файл и выводит рейтинг преступлений за 2015 год
'''
c = collections.Counter()
with open('crimes.csv') as file:
    crimes = csv.DictReader(file)
    # Читаем файл
    for row in crimes:
        # Отсеиваем по 2015 году
        if '2015' in row['Date']:
            # Счётчиком считаем
            c[row['Primary Type']] += 1
print('Самое частое преступление в 2015:', *c.most_common(1)[0])
