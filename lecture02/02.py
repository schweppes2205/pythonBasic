"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

from random import randint

my_list = []
user_wish = input("do you want to input data manually or you want to generate the data randomly? Please enter \"manually\" or \"surprise me\": ")
if user_wish == "manually":
    while True:
        try:
            list_length = int(input("Please enter the list length: "))
            break
        except ValueError:
            print("Please enter digits only.")
    for i in range(0,list_length):
        my_list.append(input("Please enter some data: "))
elif user_wish == "surprise me":
    for i in range(1, randint(11, 20)):
        my_list.append(randint(1, 100))
else:
    print("Please enter \"manually\" or \"surprise me\" next time")
    exit()
print(f"variable before any changes:\n{my_list}")
for i in range(0, len(my_list) - 1, 2):
    temp = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = temp
print(f"variable after changes:\n{my_list}")