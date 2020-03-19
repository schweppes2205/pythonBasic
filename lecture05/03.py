"""
3. Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов. Определить, кто из сотрудников
имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
подсчет средней величины дохода сотрудников.
"""

from os import path
from statistics import mean

user_data_dict = {}
with open(f"{path.join(path.dirname(__file__), '03_task_text')}", "r", encoding="utf-8") as file_descriptor:
    for line in file_descriptor:
        user_data_dict[line.split()[0]] = int(line.split()[1])
employees_with_low_salary = {name: salary for (name, salary) in user_data_dict.items() if salary <= 20000}
print(f"users with salary lower than 15000:")
for i in employees_with_low_salary.keys():
    print(i)
print(f"Average salary: {mean(user_data_dict.values())}")
