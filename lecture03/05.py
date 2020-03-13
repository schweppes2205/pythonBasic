"""
5. Программа запрашивает у пользователя строку чисел, разделенных
пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова
нажать Enter. Сумма вновь введенных чисел будет добавляться к уже
подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после
нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
"""
global_sum = 0

while True:
    end = False
    user_input = input("Please enter a string with positive numbers divided by space: ").split()
    if len(user_input) == 1 and not user_input[0].isdigit():
        exit()
    else:
        digits_from_input = []
        for input_item in user_input:
            if input_item.isdigit():
                digits_from_input.append(int(input_item))
            else:
                end = True
                break
        global_sum += sum(digits_from_input)
        print(global_sum)
        if end:
            exit()
