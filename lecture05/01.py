"""
1. Создать программно файл в текстовом формате, записать в него
построчно данные, вводимые пользователем. Об окончании ввода данных
свидетельствует пустая строка.
"""

from os import path

with open(f"{path.join(path.dirname(__file__), 'text.txt')}", "a+") as file_descriptor:
    while True:
        user_input = input("Please enter some text: ")
        if not user_input:
            break
        else:
            file_descriptor.writelines(f"{user_input}\n")