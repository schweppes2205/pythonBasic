"""
3. Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(a: int, b: int, c: int) -> int:
    """
    Sum two max variables
    :param a: int
    :param b: int
    :param c: int
    :return: int
    """
    return sum(sorted([a, b, c])[-2::1])


print(my_func(1, 2, 3))
print(my_func(c=1, b=2, a=3))