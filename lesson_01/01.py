duration = int(input('Введите целое число секунд для перевода в формат "X дн X час X мин X сек": '))
minute = 60
hour = 3600
day = 86400

# 1st variant: w/o list
# if duration < minute:
#     print(f"{duration} сек")
# if duration < hour:
#     print(f"{duration // minute} мин "
#           f"{duration % minute} сек")
# if duration < day:
#     print(f"{duration // hour} час "
#           f"{duration % hour // minute} мин "
#           f"{duration % hour % minute} сек")
# else:
#     print(f"{duration // day} дн "
#           f"{duration % day // hour} час "
#           f"{duration % day % hour // minute} мин "
#           f"{duration % day % hour % minute} сек")

# 2nd variant: with list
units_of_time = [day, hour, minute]
time_list = []
for _ in units_of_time:
    if duration // day:
        time_list.append(f"{duration // day} дн ")
    if duration % day // hour:
        time_list.append(f"{duration % day // hour} час ")
    if duration % day % hour // minute:
        time_list.append(f"{duration % day % hour // minute} мин ")
    if duration % day % hour % minute:
        time_list.append(f"{duration % day % hour % minute} сек")
        break

print("".join(time_list))
