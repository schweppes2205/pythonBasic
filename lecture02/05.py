"""
5. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел. У пользователя необходимо
запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
с одинаковыми значениями, то новый элемент с тем же значением должен
разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""
from random import randint

# my_list = [7, 5, 3, 3, 2]
my_list = []
for i in range(1, randint(11, 20)):
    my_list.append(randint(1, 100))
my_list = sorted(my_list, reverse=True)
print(f"Here is the list of ranges: {my_list}")
while True:
    while True:
        try:
            user_input = int(input("Please enter some number i'll put it to the list in the according place: "))
            break
        except ValueError:
            print("Please enter digit only")
            continue
    value_count = my_list.count(user_input)
    if value_count > 0:
        # my_list.insert(my_list.index(user_input), user_input)  # put user_input in front of the same element
        my_list.insert(my_list.index(user_input) + value_count, user_input) # put user_input after all equal elements
    else:
        my_list.append(user_input)
        my_list = sorted(my_list, reverse=True)
    print(f"here is what we have: {my_list}")


