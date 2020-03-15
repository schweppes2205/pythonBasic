"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать
формулу: (выработка в часах * ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

try:
    _, working_hours, salary, premium, = argv
except ValueError:
    print("Seems like you forgot one parameter to pass")
    exit()
try:
    print(int(working_hours) * int(salary) + int(premium))
except TypeError:
    print("Please try digits next time")
