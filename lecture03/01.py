"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def my_division(a: float, b: float):
    """
    Division of variable 'a' by variable 'b'
    :param a: float
    :param b: float zero is not possible
    :return:
    """
    return a / b if b != 0 else "please enter non-zero variable"


print(my_division(a=1, b=0))
print(my_division(1, 2))
print(my_division(b=0, a=2))
print(my_division(0, 2))


