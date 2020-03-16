"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с
указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка,
определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
from itertools import count
from time import sleep

try:
    user_input = int(input("Please enter a number: "))
except ValueError:
    print("Please enter digits only next time.")
    exit()
for i in count(user_input):
    print(i)
    sleep(1)
