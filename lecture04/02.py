"""
2. Представлен список чисел. Необходимо вывести элементы исходного
списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
"""
from random import randint


def my_generator(some_list):
    for i in range(1, len(some_list)):
        if some_list[i] > some_list[i - 1]:
            yield some_list[i]


original_list = [randint(1, 1000) for i in range(10)]
new_list = my_generator(original_list)

print(f"original list: {original_list}\nnew list: {list(new_list)}")
