class Wear:
    def __init__(self, title):
        self.con = float
        self.title = title

    @property
    def consumption(self):
        return self.con

    def __str__(self):
        return self.title

    def __add__(self, other):
        return Wear(self.con + other.con)


class Coat(Wear):
    def __init__(self, title, size):
        super().__init__(title)
        self.size = size

    @property
    def consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Wear):
    def __init__(self, title, height):
        super().__init__(title)
        self.height = height

    @property
    def consumption(self):
        return round(self.height * 2 + 0.3, 2)


red_coat = Coat("Red coat", 46)
black_coat = Coat("Black coat", 50)
s_grey_suit = Suit("Small grey suit", 1.4)
print(red_coat, f"(size: {red_coat.size})", red_coat.consumption)
print(black_coat, f"(size: {black_coat.size})", black_coat.consumption)
print(s_grey_suit, f"(height: {s_grey_suit.height})", s_grey_suit.consumption)
print("Total:", red_coat.consumption + black_coat.consumption + s_grey_suit.consumption)
