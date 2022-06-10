FILE_ENCODING = 'utf-8'

full_names = []
hobbies_list = []

with open('users.csv', 'r', encoding=FILE_ENCODING) as users:
    for user in users:
        full_names.append(user.strip().replace(",", " "))

with open('hobby.csv', 'r', encoding=FILE_ENCODING) as hobbies:
    for hobby in hobbies:
        hobbies_list.append(hobby.strip())

result = {}

for user in range(len(full_names)):

    try:
        username = full_names[user]
    except IndexError:
        break

    try:
        hobby = hobbies_list[user]
    except IndexError:
        hobby = None

    result[username] = hobby

with open('result.txt', 'w', encoding=FILE_ENCODING) as f:
    f.write(str(result))
