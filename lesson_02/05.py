prices = [57.8, 46.51, 97, 23, 11.05,
          43.6, 4, 234, 3, 211,
          19, 322.11, 31, 28.5, 66.55,
          123, 78, 36.6, 42.2, 45.32,
          ]

# unsorted
formatted_prices = ""
for price in prices:
    formatted_price = float(price)
    rub = round(formatted_price)
    kop = int(str(formatted_price).split('.')[1])
    if kop < 10:
        kop = '0' + str(kop)
    formatted_prices += f"{rub} руб {kop} коп, "

print(f"list id= {id(prices)}")
print(formatted_prices[:-2:], "\n")

# sorted ascending
formatted_prices = ""
prices.sort()
for price in prices:
    formatted_price = float(price)
    rub = round(formatted_price)
    kop = int(str(formatted_price).split('.')[1])
    if kop < 10:
        kop = '0' + str(kop)
    formatted_prices += f"{rub} руб {kop} коп, "

print(f"list id= {id(prices)}")
print(formatted_prices[:-2:], "\n")

# sorted descending
formatted_prices = ""
desc_prices = prices[::-1]
for price in desc_prices[:5]:
    formatted_price = float(price)
    rub = round(formatted_price)
    kop = int(str(formatted_price).split('.')[1])
    if kop < 10:
        kop = '0' + str(kop)
    formatted_prices += f"{rub} руб {kop} коп, "

print(f"list id= {id(desc_prices)}")
print(formatted_prices[:-2:], "\n")

