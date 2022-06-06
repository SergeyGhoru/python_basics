def odd_nums(stop):
    current = 1
    while current <= stop:
        yield current
        current += 2


odd_to_15 = odd_nums(15)

for i in range (10):
    print(next(odd_to_15))
