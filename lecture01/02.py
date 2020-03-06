"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
user_input = input("Please enter amount of seconds: ")
while not user_input.isdigit():
    user_input = input("Please enter digits only: ")
else:
    user_input = int(user_input)
    seconds = user_input % 60
    minutes = (user_input // 60) % 60
    hours  = user_input // 3600
    print(f"{user_input} seconds equal to {hours:02}:{minutes:02}:{seconds:02} (hh:mm:ss)")