"""
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны
передаваться при создании экземпляра класса. Атрибуты сделать
защищенными. Определить метод расчета массы асфальта, необходимого
для покрытия всего дорожного полотна. Использовать формулу:
длинаширинамасса асфальта для покрытия одного кв метра дороги
асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу
метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_weight(self, weight_per_cubic_centimeter, depth):
        return self._length * self._width * weight_per_cubic_centimeter * depth


user_input = input("Please provide length, width, weight per cubic centimeter, depth separated by space: ").split()
try:
    user_input = [int(x) for x in user_input]
except TypeError:
    print("Please try digits next time.")
    exit()
a = Road(length=user_input[0], width=user_input[1])
print(a.asphalt_weight(weight_per_cubic_centimeter=user_input[2], depth=user_input[3]))
