from time import sleep
import sys


class TrafficLight:
    def __init__(self):
        self.colors = ["Красный", "Жёлтый", "Зелёный"]
        self.timing = [7, 2, 7]
        self.__color = str
        self.__prev_color = self.colors[2]
        self.ERR_ROTATION = "[СБОЙ] Нарушен порядок чередования цветов"

    def running(self, hacked=False):

        while True:

            for index in range(len(self.colors)):
                self.__color = self.colors[index]
                print(f"Включаем {self.__color}")
                if hacked:
                    import random

                    self.__color = random.choice(self.colors)
                    print(f"Выбран случайный цвет {self.__color}")
                if (
                    self.__color == self.colors[index]
                    and self.__prev_color == self.colors[index - 1]
                ):
                    print(self.__color)
                    self.__prev_color = self.__color
                else:
                    print(self.ERR_ROTATION)
                    sys.exit(2)
                sleep(self.timing[index])


light = TrafficLight()
# 1-й вариант запуска - нормальный режим
light.running()
# 2-й вариант запуска - сбойный
# light.running(hacked=True)
