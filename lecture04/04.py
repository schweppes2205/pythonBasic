"""
4. Представлен список чисел. Определить элементы списка, не имеющие
повторений. Сформировать итоговый массив чисел, соответствующих
требованию. Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
"""

from random import randint
from collections import Counter


def my_generator(some_list, some_dict):
    for i in some_list:
        if some_dict[i] == 1:
            yield i


original_list = [randint(1, 10) for i in range(randint(10, 20))]
print(f"original list: {original_list}")
print(Counter(original_list))
new_list = my_generator(original_list, Counter(original_list))
print(list(new_list))
