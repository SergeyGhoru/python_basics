class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return f"{self.speed}"

    def go(self, speed):
        self.speed = speed
        print(f"{self.name} поехала со скростью {self.speed} км/ч")

    def stop(self):
        self.speed = 0
        print(f"{self.name} остановилась")

    def turn(self, direct):
        print(f"{self.name} повернула {direct}")


class TownCar(Car):
    def show_speed(self):
        s_limit = 60
        if self.speed > s_limit:
            return f"{self.speed} (ПРЕВЫШЕНИЕ {s_limit})"
        return f"{self.speed}"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        s_limit = 40
        if self.speed > s_limit:
            return f"{self.speed} (ПРЕВЫШЕНИЕ {s_limit})"
        return f"{self.speed}"


class PoliceCar(Car):
    pass


ferrari = SportCar(100, "красный", "Ferrari F430", False)
probox = TownCar(110, "черный", "Toyota Probox", False)
komatsu = WorkCar(31, "желтый", "Komatsu wb93r", False)
corolla = PoliceCar(-5, "белый", "Toyota Corolla", True)

for car in [ferrari, probox, komatsu, corolla]:
    print(
        f"{car.name} скорость: '{car.show_speed()}', цвет: {car.color}, полицейская: '{car.is_police}' тип: {car.__class__}"
    )
    car.turn("направо")
    car.stop()
    print(f"{car.name} скорость: '{car.show_speed()}'")
    car.go(150)
    print(f"{car.name} скорость: '{car.show_speed()}'")
    print("\n")
