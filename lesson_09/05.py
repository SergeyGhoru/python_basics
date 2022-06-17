class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Используется: {self.title}, пишем ручкой")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Используется: {self.title}, рисуем карандашом")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Используется: {self.title}, помечаем маркером")


black_pen = Pen("Черная ручка")
yellow_pencil = Pencil("Жёлтый карандаш")
blue_handle = Handle("Синий маркер")

for stationery in [black_pen, yellow_pencil, blue_handle]:
    stationery.draw()
