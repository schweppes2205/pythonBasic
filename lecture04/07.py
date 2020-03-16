"""
7. Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться
объект-генератор. Функция должна вызываться следующим образом:
for el in fibo_gen(). Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например,
факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from math import factorial


def my_gen(some_number):
    j = 1
    for i in str(factorial(some_number)):
        yield i
        j += 1
        if j == 16:
            break


try:
    user_input = int(input("Please enter some number: "))
except ValueError:
    print("Enter digits only next time.")
    exit()

for i in enumerate(my_gen(user_input), 1):
    print(i)
