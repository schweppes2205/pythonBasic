"""
1. Создать класс TrafficLight (светофор) и определить у него один
атрибут color (цвет) и метод running (запуск). Атрибут реализовать
как приватный. В рамках метода реализовать переключение светофора в
режимы: красный, желтый, зеленый. Продолжительность первого состояния
(красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно
осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при
его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from random import choice
from time import sleep


class TrafficLight:
    __colors = ("red", "yellow", "green")

    def __init__(self, green_light_delay):
        self.__green_light_delay = green_light_delay
        self.__yellow_light_delay = 2
        self.__red_light_delay = 7

    def running(self):
        next_light = choice(TrafficLight.__colors)
        while True:
            if next_light == "red":
                print(next_light)
                next_light = choice(TrafficLight.__colors)
                sleep(self.__red_light_delay)
            else:
                print("LIGHT ERROR")
                exit()
            if next_light == "yellow":
                print(next_light)
                next_light = choice(TrafficLight.__colors)
                sleep(self.__red_light_delay)
            else:
                print("LIGHT ERROR")
                exit()
            if next_light == "green":
                print(next_light)
                next_light = choice(TrafficLight.__colors)
                sleep(self.__red_light_delay)
            else:
                print("LIGHT ERROR")
                exit()


a = TrafficLight(10)
a.running()
