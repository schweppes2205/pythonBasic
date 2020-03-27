"""
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. В его конструкторе инициализировать
параметр, соответствующий количеству ячеек клетки (целое число). В классе
должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__truediv__()). Данные методы должны применяться только к клеткам
и выполнять увеличение, уменьшение, умножение и целочисленное
(с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
разность количества ячеек двух клеток больше нуля, иначе выводить
соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки
определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки
определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр
класса и количество ячеек в ряду. Данный метод позволяет организовать
ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество
ячеек между \n равно переданному аргументу. Если ячеек на формирование
ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в
ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell():
    def __init__(self, count):
        self.count = count

    @property
    def get_count(self):
        return self.count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        result = self.count - other.count
        return result if result > 0 else "the result is <= 0"

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count

    def make_order(self, base):
        result = ""
        for i in range(self.count // base):
            result += "*" * base + "\n"
        if self.count % base != 0:
            result += "*" * (self.count % base)
        return result


my_cell_1 = Cell(10)
print(f"Order function result:\n{my_cell_1.make_order(6)}")
my_cell_2 = Cell(15)
my_cell_3 = Cell(my_cell_1 + my_cell_2)
try:
    my_cell_4 = Cell(my_cell_1 - my_cell_2)
except:
    pass
try:
    my_cell_5 = Cell(my_cell_2 - my_cell_1)
except:
    pass
my_cell_6 = Cell(my_cell_1 * my_cell_2)
my_cell_7 = Cell(my_cell_1 / my_cell_2)
my_cell_8 = Cell(my_cell_2 / my_cell_1)
print(f"Sum of cells {my_cell_1.count} and {my_cell_2.count} : {my_cell_3.get_count}")
print(f"Subtraction of cells {my_cell_1.get_count} and {my_cell_2.get_count} : {my_cell_4.get_count}")
print(f"Another Subtraction of cells {my_cell_2.get_count} and {my_cell_1.get_count} : {my_cell_5.get_count}")
print(f"Multiply of cells {my_cell_1.get_count} and {my_cell_2.get_count} : {my_cell_6.get_count}")
print(f"Division of cells {my_cell_1.get_count} and {my_cell_2.get_count} : {my_cell_7.get_count}")
print(f"Another Division of cells {my_cell_2.get_count} and {my_cell_1.get_count} : {my_cell_8.get_count}")
