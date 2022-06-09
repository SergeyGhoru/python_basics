from tarfile import ENCODING
import requests

FILENAME = 'nginx_logs.log'
FILE_ENCODING = 'utf-8'
URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(URL)

with open(FILENAME, 'w', encoding=FILE_ENCODING) as f:
    f.write(response.text)

result = []

with open(FILENAME, 'r', encoding=FILE_ENCODING) as logfile:
    for line in logfile:
        splitted_line = line.split()
        result.append((splitted_line[0], splitted_line[5], splitted_line[6]))

print(result[0], result[1], result[2])
print(len(result))
# print(result)
