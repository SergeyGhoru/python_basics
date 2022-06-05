from utils import currency_rates
import sys

help = "Give 1 argument - valute code e. g. 'USD' or 'gbp' to get currency rate to RUR"


if len(sys.argv) > 2 or len(sys.argv) == 1:
    print(help)
else:
    print(currency_rates(sys.argv[1]))
