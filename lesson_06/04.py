FILE_ENCODING = 'utf-8'


def next_hobby(cursor: int):
    with open('hobby.csv', 'r', encoding=FILE_ENCODING) as hobbies:
        hobbies.seek(cursor)
        hobby = hobbies.readline().strip()
        cursor = hobbies.tell()
    return hobby, cursor


def write_record(username: str, hobby: str, filename: str):
    with open(filename, 'a', encoding=FILE_ENCODING) as f:
        f.write(f"{username}: {hobby}\n")


with open('users.csv', 'r', encoding=FILE_ENCODING) as users:
    cursor = 0
    for user in users:
        username = user.strip().replace(",", " ")
        hobby, cursor = next_hobby(cursor)
        write_record(username=username, hobby=hobby, filename='users_hobby.txt')
