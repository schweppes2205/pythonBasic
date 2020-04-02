"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие
за приём оргтехники на склад и передачу в определенное подразделение
компании. Для хранения данных о наименовании и количестве единиц
оргтехники, а также других данных, можно использовать любую подходящую
структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
вводимых пользователем данных. Например, для указания количества
принтеров, отправленных на склад, нельзя использовать строковый тип
данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад
оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

"""
Equipmet - абстрактный класс для всей оргтехники
Printer\Scanner его наследники
Xerox наследник принтера и сканера

Warehouse - склад. у него есть своя база в виде словаря
{
    "Printer":[Printer object,Printer object...]
    "Scanner":[Scanner object,Scanner objects...]
    "Xerox":[Xerox object,Xerox object...]
} 
Склад может принимать оборудование в виде листа объектов
Склад может отгружать оборудование в виде листа объектов

Office - оффис. Также как склад имеет базу данных в виде:
{
    "Printer":[[Printer object, Source Warehouse]...]
    "Scanner":[[Scanner object, Source Warehouse]...]
    "Xerox":[[Xerox object, Source Warehouse]...]
} 
Умеет только принимать оборудование.
"""

from abc import ABC, abstractmethod
from random import choice, randint
from string import ascii_letters, digits
from os import path


def generate_name():
    # return ''.join(choice(ascii_letters) for i in range(15))
    return choice(name_list)


def generate_id():
    return ''.join(choice(digits) for i in range(15))


class Equipment(ABC):
    @abstractmethod
    def __init__(self):
        self._name = generate_name()
        self._id = generate_id()

    @abstractmethod
    def get_name(self):
        pass


class Printer(Equipment):
    def __init__(self):
        super().__init__()

    @property
    def get_name(self):
        return f'{self._name};{self._id}'

    def printer_to_print(self, prnt_str):
        print(f'I\'m {self._name} with id:{self._id}. I\'m printing {prnt_str}')


class Scanner(Equipment):
    def __init__(self):
        super().__init__()

    @property
    def get_name(self):
        return f'{self._name};{self._id}'

    def scanner_to_scan(self):
        print(f"I'm {self._name} with id:{self._id} and I'm scanning. bzzzzzzzzz")


class Xerox(Printer, Scanner):
    pass


class Warehouse:
    __wh_count = 0
    __wh_id_list = []

    def __init__(self):
        self.__name = generate_name()
        self.__id = generate_id()
        self.__wh_equipment_db = {}
        Warehouse.__wh_count += 1
        Warehouse.__wh_id_list.append(self.__id)

    def __str__(self, details=False):
        result = f'{self.get_wh_name_id}.\n'
        for i in self.__wh_equipment_db.keys():
            result += f'{i}:\n'
            if details:
                for j in self.__wh_equipment_db[i]:
                    result += f'{j.get_name}\n'
            else:
                result += f'{len(self.__wh_equipment_db[i])} items.\n'
        return result

    @property
    def get_wh_name_id(self):
        return f'{self.__name};{self.__id}'

    def get_equipment_count(self, equipment):
        return len(self.__wh_equipment_db[equipment])

    @classmethod
    def get_wh_count(cls):
        return cls.__wh_count

    @classmethod
    def get_wh_id_list(cls):
        return cls.__wh_id_list

    def wh_income(self, income_list):
        for i in income_list:
            try:
                self.__wh_equipment_db[type(i).__name__].append(i)
            except KeyError:
                self.__wh_equipment_db[type(i).__name__] = [i]

    def wh_outcome(self, **kwargs):
        result = []
        for i in kwargs.keys():
            if len(self.__wh_equipment_db[i]) >= kwargs[i]:
                for j in range(kwargs[i]):
                    result.append(self.__wh_equipment_db[i].pop())
            else:
                print(f"There is only {self.get_equipment_count(i)} of {i} left in warehouse")
        return result


class Office:
    __office_count = 0
    __office_id_list = []

    def __init__(self):
        self.__name = generate_name()
        self.__id = generate_id()
        self.__office_equipment_db = {}
        Office.__office_count += 1
        Office.__office_id_list.append(self.__id)

    def __str__(self, details=False):
        result = f'{self.get_office_name_id}.\n'
        for i in self.__office_equipment_db.keys():
            result += f'{i}:\n'
            if details:
                for j in self.__office_equipment_db[i]:
                    result += f'{j[0].get_name} came from warehouse {j[1].get_wh_name_id}\n'
            else:
                result += f'{len(self.__office_equipment_db[i])} items.\n'
        return result

    @property
    def get_office_name_id(self):
        return f"{self.__name};{self.__id}"

    @classmethod
    def get_office_count(cls):
        return cls.__office_count

    @classmethod
    def get_office_id_list(cls):
        return cls.__office_id_list

    def office_income(self, income_list, wh):
        for i in income_list:
            try:
                self.__office_equipment_db[type(i).__name__].append([i, wh])
            except KeyError:
                self.__office_equipment_db[type(i).__name__] = [[i, wh]]
        pass


if __name__ == "__main__":
    name_list = []  # variable to store names for name generator for all elements with names
    with open(f'{path.join(path.dirname(__file__), "04_05_06_names")}', encoding="utf-8") as f:
        for line in f:
            name_list.append(line.split("\n")[0])

    ### Lets generate a database for warehouse
    equipment_list = [Printer() for i in range(randint(1, 100))]
    equipment_list.extend([Scanner() for i in range(randint(1, 100))])
    equipment_list.extend([Xerox() for i in range(randint(1, 100))])
    wh1 = Warehouse()
    ### put that into warehouse database.
    wh1.wh_income(equipment_list)
    ### Creating a new office
    new_office = Office()
    print("Hello my friend. By that moment we've generated the next elements for you to play:")
    print(f"Here is a warehouse and it's content:", wh1)
    print(f"Here is a new office", new_office)
    print("Now let's deliver some equipment from the warehouse to the office")
    user_input = input("Please enter 3 numbers separated by space for how much "
                       "equipment do you want to deliver accordingly to printer scanner xerox: ")
    user_input = user_input.split()
    outcome_data = {"Printer": int(user_input[0]), "Scanner": int(user_input[1]), "Xerox": int(user_input[2])}
    new_office.office_income(wh1.wh_outcome(**outcome_data), wh1)
    print("Lets see what has changed:")
    print(wh1)
    print(new_office)
    print("Some details for the new office")
    print(new_office.__str__(details=True))
