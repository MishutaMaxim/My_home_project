"""
Дана строка, состоящая из слов, разделенных пробелами.
Напишите программу, которая подсчитывает количество слов в этой строке.
"""


def words_counter(string: str):
    return len(string.split())


string = input()
print(words_counter(string))
