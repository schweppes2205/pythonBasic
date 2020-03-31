"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс,
описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники
(принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""

from abc import ABC, abstractmethod


class Equipment(ABC):
    @abstractmethod
    def __init__(self, equipment_name):
        self.equipment_name = equipment_name


class Printer(Equipment):
    def __init__(self, equipment_name):
        super().__init__(equipment_name)

    @property
    def get_name(self):
        return self.equipment_name

    @staticmethod
    def printer_to_print(print_this_please):
        print(print_this_please)


class Scanner(Equipment):
    def __init__(self, equipment_name):
        super().__init__(equipment_name)

    @property
    def get_name(self):
        return self.equipment_name

    @staticmethod
    def scanner_to_scan():
        print("I'm scanning. bzzzzzzzzz")


class Xerox(Printer, Scanner):
    pass


if __name__ == "__main__":
    printer = Printer("i'm printer")
    print(printer.get_name)
    scanner = Scanner('i\'m scanner')
    Printer.printer_to_print(scanner.get_name)
    xerox = Xerox('i\'m XEROX motherfather')
    Xerox.printer_to_print(xerox.get_name)
    Xerox.scanner_to_scan()
