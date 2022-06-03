def thesaurus(*args: tuple):
    """
    Input: tuple with proper names
    Return: dictionary: {"first_letter_of_name": [list of names starting with that letters]}
    """
    res = dict()

    for item in args:
        res[item[0]] = []

    for item in args:
        prev = res[item[0]]
        prev.append(item)
        res[item[0]] = list(set(prev))

    return res

# unsorted
unsorted = thesaurus("Иван", "Мария", "Петр", "Илья", "Илья", "Андрей")
print(f"Unsorted:\n{unsorted}")

# sorted
to_sort = list(thesaurus("Иван", "Мария", "Петр", "Илья", "Илья", "Андрей").items())
print(f"Sorted:\n {sorted(to_sort, key=lambda x: x[0])}")
