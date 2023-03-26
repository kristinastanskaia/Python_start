"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time
import colorama
from colorama import Fore, Style


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        a._TrafficLight__color = 'RED'
        print(Fore.RED + a._TrafficLight__color)
        time.sleep(7)
        a._TrafficLight__color = 'YELLOW'
        print(Fore.YELLOW + a._TrafficLight__color)
        time.sleep(2)
        a._TrafficLight__color = 'GREEN'
        print(Fore.GREEN + a._TrafficLight__color)
        time.sleep(5)
        print(Style.RESET_ALL + 'Stop!')


a = TrafficLight(' ')
a.running()
