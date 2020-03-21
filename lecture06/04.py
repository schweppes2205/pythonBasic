"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go,
stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При
значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните
доступ к атрибутам, выведите результат. Выполните вызов методов и также
покажите результат.
"""
from random import randint, choice


class Car:
    def __init__(self, color, name, is_police: bool = False):
        self._speed = 0
        self._color = color
        self._name = name
        self._is_police = is_police
        self._if_go = False

    def go(self):
        self._if_go = True
        self._speed = randint(1, 100)
        print(f"{self._name.title()} is running now")

    def stop(self):
        self._speed = 0
        self._if_go = False
        print(f"{self._name.title()} is stopped now")

    def turn(self):
        print(f"{self._name.title()} turned to the {choice(('right','left'))}")

    def show_speed(self):
        print(f"{self._name.title()} is running {self._speed} mph now.") if self._if_go else print(
            f"{self._name.title()} is not running now. Please start the engine")


class TownCar(Car):
    def show_speed(self):
        if self._if_go:
            if self._speed > 60:
                print(f'{self._name.title()} speed is too high - {self._speed}. '
                      f'Should  be lower than 60 mph. I\'ll stop it for you')
                self.stop()
            else:
                print(f"{self._name.title()} is running {self._speed} mph now.")
        else:
            print(f"{self._name.title()} is not running now. Please start the engine")


class SportCar(Car):
    def go(self):
        self._if_go = True
        self._speed = randint(100, 500)
        print(f"{self._name.title()} is running now")


class WorkCar(Car):
    def show_speed(self):
        if self._if_go:
            if self._speed > 40:
                print(f'{self._name.title()} speed is too high - {self._speed}. '
                      f'Should  be lower than 40 mph. I\'ll stop it for you')
                self.stop()
            else:
                print(f"{self._name.title()} is running {self._speed} mph now.")
        else:
            print(f"{self._name.title()} is not running now. Please start the engine")


class PoliceCar(Car):
    def __init__(self, color, name, is_police: bool = True):
        super().__init__(color, name, is_police)


car_a = TownCar("brown", "городская ласточка")
car_a.show_speed()
car_a.go()
car_a.show_speed()
car_b = WorkCar("gray", "рабочая лошадка")
car_b.go()
car_b.show_speed()
car_c = PoliceCar("pink", "полицейская ласточка")
car_c.go()
car_c.turn()
car_c.show_speed()
car_d = SportCar("black", "гоночная ласточка")
car_d.show_speed()
car_d.go()
car_d.show_speed()

