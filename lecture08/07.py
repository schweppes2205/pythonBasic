"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число», реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата.
"""


class ComlexNumbers:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def get_x(self):
        return self.__x

    @property
    def get_y(self):
        return self.__y

    def __str__(self):
        return f"{self.__x}+{self.__y}i" if self.__y > 0 else f"{self.__x}{self.__y}i"

    def __add__(self, other):
        return ComlexNumbers(self.__x + other.get_x, self.__y + other.get_y)

    def __sub__(self, other):
        return ComlexNumbers(self.__x - other.get_x, self.__y - other.get_y)


coml01 = ComlexNumbers(1, 2)
print(coml01)
coml02 = ComlexNumbers(3, 4)
print(coml02)

print(coml01 + coml02)
print(coml01 - coml02)
