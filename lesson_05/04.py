def more_than_prev(elements):
    curr = 0
    prev = 0

    while curr < len(elements):
        curr_item = elements[curr]

        if curr == 0:
            curr += 1
            prev = curr_item

        elif curr_item > prev:
            yield elements[curr]
            curr += 1
            prev = curr_item

        else:
            curr += 1
            prev = curr_item


def release_generator(g):
    res = []

    for _ in range(20):
        try:
            res.append(next(g))
        except StopIteration:
            break

    return res


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = release_generator(more_than_prev(src))
print(result)
