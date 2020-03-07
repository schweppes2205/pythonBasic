"""
4. Пользователь вводит строку из нескольких слов, разделённых
пробелами. Вывести каждое слово с новой строки. Строки необходимо
пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_string = input("Please enter anything you want. Please use space to separate words. Do not limit yourself: ")
list_from_user_input = user_string.split()
for i,word in enumerate(list_from_user_input,1):
    print(f"{i} : {word[0:10]}")
