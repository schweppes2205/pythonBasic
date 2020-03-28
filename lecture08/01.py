"""
1. Реализовать класс «Дата», функция-конструктор которого должна
принимать дату в виде строки формата «день-месяц-год». В рамках класса
реализовать два метода. Первый, с декоратором @classmethod, должен
извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу
полученной структуры на реальных данных.
"""
from datetime import datetime


class My_date():
    def __init__(self, d, m, y):
        self.day, self.month, self.year = d, m, y

    @classmethod
    def from_string(cls, date_str):
        d, m, y = date_str.split("-")
        return cls(int(d), int(m), int(y))

    @staticmethod
    def validate_date(d, m, y):
        try:
            datetime.strptime(f"{d}-{m}-{y}", '%d-%m-%Y')
            print(f"Date {d}-{m}-{y} is valid")
        except:
            print(f"Date {d}-{m}-{y} is not valid. Please check that it is dd-mm-yyyy "
                  f"and it's correct amount of days in month and months in year.")


my_date_1 = My_date(1, 2, 3)
print(f"{my_date_1.day}.{my_date_1.month}.{my_date_1.year}")
my_date_2 = My_date.from_string("3-2-1")
print(f"{my_date_2.day}.{my_date_2.month}.{my_date_2.year}")
My_date.validate_date(28, 2, 2200)
My_date.validate_date(31, 2, 2200)
