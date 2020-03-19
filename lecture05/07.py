"""
7. Создать (не программно) текстовый файл, в котором каждая строка
должна содержать данные о фирме: название, форма собственности, выручка,
издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней
прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью. Если фирма получила
убытки, также добавить ее в словарь (со значением убытков).
Пример списка:
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json
from os import path
from statistics import mean

result_profit = []
profit_data_dict = {}
result_waste = []
waste_data_dict = {}
raw_data = []
with open(f"{path.join(path.dirname(__file__), '07_task_text')}", encoding="utf-8") as file_descriptor:
    for line in file_descriptor:
        raw_data.append(line.split())

for item in raw_data:
    try:
        if int(item[2]) - int(item[3]) > 0:
            profit_data_dict[item[0]] = int(item[2]) - int(item[3])
        else:
            waste_data_dict[item[0]] = int(item[2]) - int(item[3])
    except TypeError:
        print("Most probably some of profit or waist data is incorrectly entered.")
if profit_data_dict:
    result_profit.append(profit_data_dict)
    result_profit.append({"average_profit": mean(profit_data_dict.values())})
if waste_data_dict:
    result_waste.append(waste_data_dict)
    result_waste.append({"average_waste": mean(waste_data_dict.values())})

with open(f"{path.join(path.dirname(__file__), '07_task_result.json')}", "a+") as file_descriptor:
    json.dump([result_profit, result_waste], file_descriptor)
# print(result_profit)
# print(result_waste)
