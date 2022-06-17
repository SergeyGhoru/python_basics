class Road:
    def __init__(self, ln, wd):
        self._length = ln
        self._width = wd

    def build(self):
        consumption = self._length * self._width * 25 * 5 / 1000
        print(
            f"Расход материала для строительства дорожного полотна "
            f"{self._length} м на {self._width} м составил {consumption} т"
        )


road = Road(5000, 20)
road.build()
road2 = Road(50000, 15)
road2.build()
