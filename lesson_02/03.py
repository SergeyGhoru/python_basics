raw_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for el in range(len(raw_list)):
    item = raw_list[el]
    # integers
    try:
        if item.startswith('+'):
            to_append = str("+{:02d}".format(int(item)))
            raw_list[el] = f'"{to_append}"'
        else:
            to_append = str("{:02d}".format(int(item)))
            raw_list[el] = f'"{to_append}"'
    # characters
    except ValueError:
        pass

print(" ".join(raw_list))
