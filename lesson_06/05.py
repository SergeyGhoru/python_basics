import sys


FILE_ENCODING = 'utf-8'
HELP = """Give 3 arguments: input filenames users, hobbies and output filename
example: python3 05.py users.csv hobby.csv users_hobby.txt"""


def next_hobby(cursor: int):
    with open(hobbies_file, 'r', encoding=FILE_ENCODING) as hobbies:
        hobbies.seek(cursor)
        hobby = hobbies.readline().strip()
        cursor = hobbies.tell()
    return hobby, cursor


def write_record(username: str, hobby: str, filename: str):
    with open(filename, 'a', encoding=FILE_ENCODING) as f:
        f.write(f"{username}: {hobby}\n")



if __name__ == "__main__":
    if len(sys.argv) != 4 or len(sys.argv) == 1:
        print(HELP)
    else:
        user_file = sys.argv[1]
        hobbies_file = sys.argv[2]
        output_file = sys.argv[3]

        with open(user_file, 'r', encoding=FILE_ENCODING) as users:
            cursor = 0
            for user in users:
                username = user.strip().replace(",", " ")
                hobby, cursor = next_hobby(cursor)
                write_record(username=username, hobby=hobby, filename=output_file)
