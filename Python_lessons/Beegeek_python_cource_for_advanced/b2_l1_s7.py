"""
Дано пятизначное или шестизначное натуральное число.
Напишите программу, которая изменит порядок его последних пяти цифр на обратный.
"""


def reverce_last_five(number: str):
    result = number[:-5] + number[:-6:-1]
    return int(result) // 1


n = input()
print(reverce_last_five(n))
