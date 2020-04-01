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

from abc import ABC, abstractmethod
from random import choice
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

    def __str__(self):
        result = f'Warehouse name: \"{self.__name}\". Warehouse id: \"{self.__id}\"'
        for i in self.__wh_equipment_db.keys():
            result += f'{i}:\n'
            for j in self.__wh_equipment_db[i]:
                result += f'{j.get_name}\n'
        return result

    @property
    def get_wh_name_id(self):
        return f'{self.__name};{self.__id}'

    @classmethod
    def get_wh_count(cls):
        return cls.__wh_count

    @classmethod
    def get_wh_id_list(cls):
        return cls.__wh_id_list

    def wh_income(self, equipment_list):
        for i in equipment_list:
            try:
                self.__wh_equipment_db[type(i).__name__].append(i)
            except KeyError:
                self.__wh_equipment_db[type(i).__name__] = [i]


class Office:
    __of_count = 0
    __of_id_list = []

    def __init__(self):
        self.__name = generate_name()
        self.__id = generate_id()
        self.__of_equipment_db = {}
        Office.__of_count += 1
        Office.__of_id_list.append(self.__id)

    def __str__(self):
        pass

    @property
    def get_of_name_id(self):
        return f"{self.__name};{self.__id}"

    @classmethod
    def get_of_count(cls):
        return cls.__of_count

    @classmethod
    def get_of_id_list(cls):
        return cls.__of_id_list

    def of_income(self, equipment_list):
        pass


if __name__ == "__main__":
    name_list = []
    with open(f'{path.join(path.dirname(__file__), "04_05_06_names")}') as f:
        for line in f:
            name_list.append(line.split("\n")[0])
    # printer = Printer()
    # print(type(printer).__name__)
    # printer.printer_to_print(printer.get_name)
    # scanner = Scanner()
    # scanner.scanner_to_scan()
    # xerox = Xerox()
    # xerox.printer_to_print("talala")
    # xerox.scanner_to_scan()
    # print(Warehouse.get_wh_count())
    # print(Warehouse.get_wh_id_list())
    equipment_list = [Printer() for i in range(10)]
    equipment_list.extend([Scanner() for j in range(10)])
    equipment_list.extend([Xerox() for j in range(10)])
    wh1 = Warehouse()
    print(wh1.get_wh_name_id)
    wh1.wh_income(equipment_list)
    print(wh1)
