class Cell:
    def __init__(self, c):
        self.count = c

    def __str__(self):
        return f"{self.count}"

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, arr):
        str_count = self.count // arr
        body = "\n".join("".join("*" for _ in range(arr)) for _ in range(str_count))
        appendix = "".join("*" for _ in range(self.count - (str_count * arr)))
        return f"\n{body}\n{appendix}"


cell_1 = Cell(12)
cell_2 = Cell(5)
print(
    f"Клетка-1: {cell_1} ячеек\nКлетка-2: {cell_2} ячеек\n"
    f"Сумма размеров клеток (add): {cell_1 + cell_2}\n"
    f"Разница размеров клеток (sub): {cell_1 - cell_2}\n"
    f"Произведение размеров клеток (mul): {cell_1 * cell_2}\n"
    f"Результат деления размеров клеток (truediv): {cell_1 / cell_2}\n"
)
print(f"Клетка-1 рядами по 5", cell_1.make_order(5), "\n")
print(f"Клетка-1 рядами по 4", cell_1.make_order(4), "\n")
print(f"Клетка-2 рядами по 2", cell_2.make_order(2), "\n")
