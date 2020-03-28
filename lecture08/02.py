"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию
деления на нуль. Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"Custom message is: {self.message}"
        else:
            return "No custom message. Just exception raise"


while True:
    while True:
        try:
            x, y = (input("Please enter 2 digits separating them with space for division. ")).split()
            x, y = int(x), int(y)
            break
        except ValueError:
            print("Please enter 2 digits only")
            continue
    try:
        if not y:
            raise MyException("it's zero division error. Please enter non-zero second value.")
        print(f"{x}/{y} will be {(x / y):.2f}")
    except MyException as e:
        print(e)
