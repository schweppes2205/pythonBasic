"""
2. Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон. Функция должна принимать параметры как именованные
аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def my_func(**kwargs) -> str:
    """
    Gather data of users name, surname, year of birth, city of birth, email, phone number
    :param kwargs:
    :return: string
    """
    return f"{kwargs.get('name', 'NoName')}, {kwargs.get('surname', 'NoSurname')}, {kwargs.get('year', 'NoYear')}, " \
           f"{kwargs.get('city', 'NoCity')}, {kwargs.get('email', 'NoEmail')}, {kwargs.get('phone', 'NoPhone')}"


user_data = {
    "name": "Semyon",
    "surname": "Shvets",
    "year": "1989",
    "city": "Classified city",
    "email": "Classified email",
    "phone": "Classified phone",
}

print(my_func(**user_data))
print(my_func())
print(my_func(name="Max",surname="Paul",year=2020))
