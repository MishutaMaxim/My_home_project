# Используя модуль datetime, написать функцию change_month, 
# которая к переданной дате прибавляет/вычитает переданное кол-во месяцев.
# Например:
#    change_month(’12.12.12’, 7) -> ’12.07.13’
#    change_month(’01.11.10’, -5) -> ’01.06.10’
def change_month(date, month_delta):
    import datetime                                                 # Импортируем datetime для работы с датами
    from dateutil.relativedelta import relativedelta                # Импортируем relativedelta для работы с месяцами
    date = datetime.datetime.strptime(date, '%d.%m.%y')             # Полученную строку обрабатываем модулем и преобразуем в дату
    if month_delta > 0:
        result = date + relativedelta(months=month_delta)           # Если параметр изменения месяца больше нуля - прибавляем дельту месяцев
    else:
        result = date - relativedelta(months=abs(month_delta))      # Если параметр изменения месяца меньше нуля - убавляем дельту месяцев
    result = result.strftime('%d.%m.%y')                            # Форматируем полученную дату в нужный вид
    return result


# print(change_month('12.12.12', 7))
# print(change_month('01.11.10', -5))


# Напишите декоратор func_time, который подсчитывает и выводит сколько времени выполняется функция, обернутая в него.
def func_time(func):
    def wrapper():
        import time
        time_start = time.time()                # Фиксируем время начала работы функции
        func()                                  # Вызываем функцию
        time_end = time.time()                  # Фиксируем время окончания работы функции
        working_time = time_end - time_start    # Вычисляем время работы
        print(f'Функция {func.__name__} выполнялась {round(working_time, 6)} сек.')
    return wrapper


@func_time
def some_func():
    for i in range(10000):
        s = i ** 3
    print('Some func is worked')


# some_func()

# Опишите класс Name. Экземпляр класса создается одной строкой, состоящей из 2-3 слов (на это должна быть проверка).
# Например: Name(‘Иванов Иван’) или Name(‘Иванов Иван Иванович’)
# Среди методов этого класса должны быть: 
# brief_name() Возвращает строку вида ‘Фамилия Имя’ (без отчества) 
# initials() Возвращает строку вида ‘Фамилия И.О.’ (фамилия и инициалы)
# strfname(format) Преобразует по переданному формату format строку, где
#     %Ф - фамилия, %ф – первая буква фамилии,
#     %И - имя, %и - первая буква имени
#     %О - отчество, %о - первая буква отчества
# Например: name.strfname(‘%И %О %ф.’) -> Иван Иванович И.
# 	    name.strfname(‘%и. %о. %Ф’) -> И. И. Иванов
class name:
    # Инициализация класса, на вход получаем строку из 2-3 слов и формируем элемент класса на их основе.
    def __init__(self, args):
        args = args.split()     # Строку преобразуем в список для работы с элементами отдельно
        if len(args) == 2:      # Проверяем количество элементов, если Отчество не указано, делаем его пустой строкой
            self.surname, self.name = args
            self.patronymic = ''
        elif len(args) == 3:
            self.surname, self.name, self.patronymic = args
        else:                   # Если количество элементов меньше 2 или больше 3 - выводим ошибку
            print('Не верное число аргументов, введите Фамилию Имя или Фамилию Имя Отчество')

    # Возвращает строку в формате Фамилия Имя (без отчества)
    def brief_name(self):
        return self.surname + ' ' + self.name

    # Возвращает строку вида ‘Фамилия И.О.’ (фамилия и инициалы)
    def initials(self):
        surname = self.surname + ' '
        name = self.name[0] + '.'
        # Проверяем наличие отчества и выводим первую букву с точкой если оно есть у элемента класса
        if len(self.patronymic) > 0:
            patronymic = self.patronymic[0] + '.'
        else:
            patronymic = ''
        # Складываем всё вместе
        result = surname + name + patronymic
        return result

    # Преобразует по переданному формату format_name строку
    def strfname(self, format_name):
        # Заменяем все элементы формата нужными данными
        format_name = format_name.replace('%И', self.name)
        format_name = format_name.replace('%и', self.name[0])
        format_name = format_name.replace('%Ф', self.surname)
        format_name = format_name.replace('%ф', self.surname[0])
        # Проверка наличия отчества у элемента класса
        if len(self.patronymic) > 0:
            format_name = format_name.replace('%О', self.patronymic)
            format_name = format_name.replace('%о', self.patronymic[0])
        else:
            format_name = format_name.replace('%О', '')
            format_name = format_name.replace('%о.', '')
        return format_name

# ivan = name('Иванов Иван')
# petr = name('Петров Петр Петрович')
# # print(ivan.brief_name())
# # print(petr.brief_name())
# # print(ivan.initials())
# # print(petr.initials())
# print(ivan.strfname('%И %ф. %О'))
# print(petr.strfname('%И %О %ф.'))
# print(petr.strfname('%Ф %и. %о.'))
