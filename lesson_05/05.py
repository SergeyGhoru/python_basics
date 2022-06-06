# from memory_profiler import profile

# @profile
def uniques_only_o_2(elements):
    not_uniques = set()

    for index in range(len(elements)):
        for index2 in range(len(elements)):
            if elements[index] == elements[index2] and index != index2:
                not_uniques.add(elements[index])

    for el in not_uniques:
        elements = list(filter(lambda a: a != el, elements))

    return elements


# @profile
def uniques_only_o_n(elements):
    elements_capped = {el:elements.count(el) for el in elements}
    return [key for key, value in elements_capped.items() if value == 1]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(uniques_only_o_2(src))
print(uniques_only_o_n(src))
