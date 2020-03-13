"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить
к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]
months_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

while True:
    try:
        month_number = int(input("Please enter a month number 1-12: "))
        if month_number > 12 or month_number < 1:
            print("Please use 1 - 12 range: ")
            continue
        break
    except ValueError:
        print("Please enter digits only.")
print(f"Solution from list is {months_list[month_number - 1]}.\nSolution from dictionary is {months_dict[month_number]}")