import sys


FILENAME = 'bakery.csv'
FILE_ENCODING = 'utf-8'
HELP = """Give 1 argument: value of new sale ("5978.5" for example)"""


def add_sale(s: float):
    with open(FILENAME, 'a', encoding=FILE_ENCODING) as f:
        f.write(f"{s}\n")


if __name__ == "__main__":
    if len(sys.argv) != 2 or len(sys.argv) == 1:
        print(HELP)
    else:
        try:
            sale = float(sys.argv[1])
            add_sale(sale)
        except ValueError:
            print(HELP)
