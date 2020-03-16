"""
5. Реализовать формирование списка, используя функцию range() и
возможности генератора. В список должны войти четные числа от 100
до 1000 (включая границы). Необходимо получить результат вычисления
произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce
from random import randint

original_list = [randint(100, 1000) for i in range(10) if i % 2 != 0]
print(f"original_list: {original_list}\nlist length: {len(original_list)}")
print(reduce(lambda x, y: x * y, original_list))