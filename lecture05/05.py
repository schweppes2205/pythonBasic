"""
5. Создать (программно) текстовый файл, записать в него программно
набор чисел, разделенных пробелами. Программа должна подсчитывать
сумму чисел в файле и выводить ее на экран.
"""

from os import path
from random import randint

with open(f"{path.join(path.dirname(__file__), '05_task_text')}", "a+") as file_descriptor:
    for i in range(randint(10, 20)):
        file_descriptor.write(f"{randint(1, 10)} ")

with open(f"{path.join(path.dirname(__file__), '05_task_text')}") as file_descriptor:
    for line in file_descriptor:
        try:
            print(sum([int(x) for x in line.split()]))
        except ValueError:
            print(f"Most probably there is some non-digital char in the file "
                  f"{path.join(path.dirname(__file__), '05_task_text')}")
