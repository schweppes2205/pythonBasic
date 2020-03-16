"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с
указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка,
определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
from itertools import cycle
from random import randint
from time import sleep

original_list = [randint(1, 100) for i in range(10)]
print(original_list)
for i in cycle(original_list):
    print(i)
    sleep(1)
