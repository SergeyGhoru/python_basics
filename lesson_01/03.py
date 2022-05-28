for num in range(1, 101):
    last_num = list(str(num)).pop()
    if last_num == '1' and num != 11:
        print(f"{num} процент")
    elif int(last_num) in range(2, 5) and num not in range(12, 15):
        print(f"{num} процента")
    else:
        print(f"{num} процентов")
