"""
На вход программе подаётся натуральное число.
Напишите программу, которая вставляет в заданное число запятые в соответствии
со стандартным американским соглашением о запятых в больших числах.
"""


def standard_american_convention(number):
    if len(number) < 4:
        return number
    else:
        return standard_american_convention(number[:-3]) + ',' + number[-3:]


n = input()
print(standard_american_convention(n))
