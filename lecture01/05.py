"""
5. Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма 
(прибыль — выручка больше издержек, или убыток — издержки больше 
выручки). Выведите соответствующее сообщение. Если фирма отработала 
с прибылью, вычислите рентабельность выручки (соотношение прибыли к 
выручке). Далее запросите численность сотрудников фирмы и определите 
прибыль фирмы в расчете на одного сотрудника.
"""
while True:
    try:
        gain = float(input("Please enter gain. Digits only: "))
        cost = float(input("Please enter cost. Digits only: "))
        break
    except ValueError:
        print('Please use only digits. Float is possible.')
        continue
if (gain > cost):
    print(f"Profit this year: Efficiency is {gain / cost:.2f}")
    while True:
        try:
            employee_count = int(input("Please enter the amount of employees: "))
            break
        except ValueError:
            print('Please use only integer.')
            continue
    print(f"Profit per worker is {(gain - cost) / employee_count:.2f}")
else:
    print(f"Loss this year: {cost - gain}")