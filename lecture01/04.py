"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""
user_input = input("Please enter some number: ")
while not user_input.isdigit():
    user_input = input("Please enter digits only. Float is not possible. Negative is not possible: ")
else:
    max_number = 0
    i = 0
    while i < len(user_input):
        if (int(user_input[i]) > max_number):
            max_number = int(user_input[i])
        i += 1
    print(max_number)
