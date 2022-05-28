raw_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for item in raw_list:
    item_separated = item.split(" ")
    item_separated.reverse()
    print(f"Привет, {item_separated[0].capitalize()}!")
