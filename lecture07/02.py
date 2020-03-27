"""
2. Реализовать проект расчета суммарного расхода ткани на производство
одежды. Основная сущность (класс) этого проекта — одежда, которая может
иметь определенное название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер
(для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать
формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить
работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике
полученные на этом уроке знания: реализовать абстрактные классы для
основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def cloth_amount(self):
        pass


class Coat(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def get_height(self):
        return self.height

    @property
    def cloth_amount(self):
        return self.height / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def get_size(self):
        return self.size

    @property
    def cloth_amount(self):
        return 2 * self.size + 0.3


my_coat = Coat(180)
my_costume = Costume(52)
print(f"To make a new coat with your height {my_coat.get_height} "
      f"we need to use {my_coat.cloth_amount:.2f} amount of cloth.\n"
      f"To make a new costume with your size {my_costume.get_size}"
      f"we need to use {my_costume.cloth_amount:.2f} amount of cloth.\n"
      f"To have all work done you need to have {(my_coat.cloth_amount + my_costume.cloth_amount):.2f} amount of cloth")
