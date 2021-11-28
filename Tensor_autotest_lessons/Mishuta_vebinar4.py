# Используя модуль datetime, написать функцию change_month, 
# которая к переданной дате прибавляет/вычитает переданное кол-во месяцев.
# Например:
#    change_month(’12.12.12’, 7) -> ’12.07.13’
#    change_month(’01.11.10’, -5) -> ’01.06.10’
def change_month(date, month_delta):
    import datetime
    day, month, year = date.split('.')
    year = '20' + year
    date = datetime.date(int(year), int(month), int(day))


# Напишите декоратор func_time, который подсчитывает и выводит сколько времени выполняется функция, обернутая в него.
def func_time(func):
    def wrapper():
        import time
        time_start = time.time()
        func()
        time_end = time.time()
        working_time = time_end - time_start
        print(f'Функция {func.__name__} выполнялась {working_time} сек.')
    return wrapper


@func_time
def some_func():
    for i in range(10000):
        s = i ** 3
    print('Some func is worked')


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
    def __init__(self, args):
        args = args.split()
        if len(args) == 2:
            self.surname, self.name = args
            self.patronymic = ''
        elif len(args) == 3:
            self.surname, self.name, self.patronymic = args
        else:
            print('Не верное число аргументов, введите Фамилию Имя или Фамилию Имя Отчество')

    def brief_name(self):
        return str(self.surname + ' ' + self.name)

    def initials(self):
        surname = self.surname + ' '
        name = self.name[0] + '.'
        patronymic = ''
        if len(self.patronymic) > 0:
            patronymic = self.patronymic[0] + '.'
        init = surname + name + patronymic
        return init

    def strfname(self, format):
        format = format.split()
        result = ''
        if format[0][1].isupper():
            result += self.surname + ' '
        elif format[0][1].islower():
            result += self.surname[0] + '. '
        else:
            return 'Ошибка формата'
        if format[1][1].isupper():
            result += self.name + ' '
        elif format[1][1].islower():
            result += self.name[0] + '. '
        else:
            return 'Ошибка формата'
        if  len(self.patronymic) > 0:
            if format[2][1].isupper():
                result += self.patronymic + ' '
            elif format[2][1].islower():
                result += self.patronymic[0] + '. '
            else:
                return 'Ошибка формата'
        return result

ivan = name('Иванов Иван')
petr = name('Петров Петр Петрович')
print(ivan.brief_name())
print(petr.brief_name())
print(ivan.initials())
print(petr.initials())
print(ivan.strfname('%И %О %ф.'))
print(petr.strfname('%И %О %ф.'))
print(petr.strfname('%и. %о. %Ф'))
