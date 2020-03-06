"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
user_input = input("Please enter some number: ")
while not user_input.isdigit():
    user_input = input("Please enter digits only. Float is not possible: ")
else:
    result = int(user_input) + int(user_input * 2) + int(user_input * 3)
    print(f"Your number is {user_input}. We sum up : {user_input} + {user_input * 2} + {user_input * 3}. The result is {result}")