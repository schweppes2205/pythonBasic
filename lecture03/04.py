"""
4. Программа принимает действительное положительное число x и целое
отрицательное число y. Необходимо выполнить возведение числа x в
степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции
возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый —
возведение в степень с помощью оператора **. Второй — более сложная
реализация без оператора **, предусматривающая использование цикла.
"""


def my_pow_func(x: float, y: int):
    """
    function with ** operator
    :param x:
    :param y:
    :return:
    """
    if x < 0 or y > 0:
        return "Please enter only positive X and only negative Y."
    else:
        return x ** y


def my_no_pow_func(x: float, y: int):
    """
    function with for cycle
    :param x:
    :param y:
    :return:
    """
    if x < 0 or y > 0:
        return "Please enter only positive X and only negative Y."
    else:
        denominator = 1
        for i in range(0, abs(y)):
            denominator *= x
        return 1 / denominator


def my_pow_with_recursion(x: float, y: int):
    """
    function used recursion
    :param x:
    :param y:
    :return:
    """
    def my_recursion_func(a, b):
        if b == 1:
            return a
        else:
            return a * my_recursion_func(a, b - 1)
    if x < 0 or y > 0:
        return "Please enter only positive X and only negative Y."
    else:
        return 1 / my_recursion_func(x, abs(y))


print(pow(6, -5))
print(my_pow_func(6, -5))
print(my_no_pow_func(6, -5))
print(my_pow_with_recursion(6, -5))
