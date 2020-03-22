"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних
класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из
классов реализовать переопределение метода draw. Для каждого из классов
методы должен выводить уникальное сообщение. Создать экземпляры классов
и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery():
    def __init__(self, name):
        self.title = name

    def draw(self):
        print("Initiating draw:")


class Pen(Stationery):
    def draw(self):
        print("i'm Pen")


class Pencil(Stationery):
    def draw(self):
        print("i'm Pencil")


class Handle(Stationery):
    def draw(self):
        print("i'm Handle")


pen = Pen("pen")
pen.draw()
pencil = Pencil("pencil")
pencil.draw()
handle = Handle("handle")
handle.draw()