class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self._income = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name="", surname="", position="", wage=0, bonus=0):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


worker_a = Position(
    name="Ольга", surname="Яковлева", position="бухгалтер", wage=500, bonus=200
)

worker_b = Position(
    name="Иван", surname="Прохоров", position="водитель", wage=400, bonus=250
)

for worker in [worker_a, worker_b]:
    print(
        f"Имя сотрудника: '{worker.get_full_name()}', "
        f"должность: '{worker.position}', "
        f"доход с учетом премии: '{worker.get_total_income()}'"
    )
