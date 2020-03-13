"""
6. Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка
из слов, разделенных пробелом. Каждое слово состоит из латинских букв
в нижнем регистре. Сделать вывод исходной строки, но каждое слово
должно начинаться с заглавной буквы. Необходимо использовать
написанную ранее функцию int_func().
"""


def int_func(some_list):
    result = ""
    for item in some_list:
        result += f"{item.title()} "
    return result


while True:
    user_input = input("Enter some words: ").split()
    if False in list(map(lambda x: True if x.isalpha() else False, user_input)):
        continue
    else:
        print(int_func(user_input))
