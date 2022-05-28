raw_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []

for item in raw_list:
    # integers
    try:
        if item.startswith('+'):
            to_append = str("+{:02d}".format(int(item)))
            new_list.append(f'"{to_append}"')
        else:
            to_append = str("{:02d}".format(int(item)))
            new_list.append(f'"{str(to_append)}"')
    # characters
    except ValueError:
        new_list.append(item)

print(" ".join(new_list))
