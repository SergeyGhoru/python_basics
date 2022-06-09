import sys


FILENAME = 'bakery.csv'
FILE_ENCODING = 'utf-8'


def read_sales(start=0, stop=None):
    sales = []
    cursor = start
    with open(FILENAME, 'r', encoding=FILE_ENCODING) as f:
        f.seek(start)

        if stop:
            while cursor < stop:
                try:
                    sales.append(float(f.readline().strip()))
                except ValueError:
                    return sales
                cursor = f.tell()
        else:
            while True:
                try:
                    sales.append(float(f.readline().strip()))
                except ValueError:
                    return sales
    return sales


if __name__ == "__main__":
    try:
        start = int(sys.argv[1]) * 7 - 7
    except IndexError:
        start = 0

    try:
        stop = int(sys.argv[2]) * 7
    except IndexError:
        stop = None

    sales = read_sales(start, stop)

    for sale in range(len(sales)):
        print(sales[sale])
