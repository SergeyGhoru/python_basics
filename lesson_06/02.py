import requests

FILENAME = 'nginx_logs.log'
FILE_ENCODING = 'utf-8'
URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(URL)


def fill_stats(f: str):
    result = {}

    with open(f, 'r', encoding=FILE_ENCODING) as log:

        for line in log:
            ip = line.split()[0]

            if ip in result:
                result[ip] += 1
            else:
                result[ip] = 0

    return result


def print_top_ip(d: dict, c: int):
    sorted_dict = {k: v for k, v in reversed(sorted(d.items(), key=lambda item: item[1]))}
    counter = 1
    print(f"Top {c} IP by requests count:\n№\tIP\t\tRequests")

    for key in sorted_dict:
        print(f"{counter}\t{key}\t{sorted_dict[key]}")
        counter += 1
        if counter > c:
            break


with open(FILENAME, 'w', encoding=FILE_ENCODING) as f:
    f.write(response.text)

stats = fill_stats(FILENAME)
print_top_ip(stats, 10)
