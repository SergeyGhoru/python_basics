tutors = [
'Иван', 'Анастасия', 'Петр', 'Сергей',
'Дмитрий', 'Борис', 'Елена'
]
klasses = [
'9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def tutor_with_klass(t, k):
    curr = 0

    while curr < len(t) and curr < len(k):
        yield t[curr], k[curr]
        curr += 1

    while curr < len(t):
        yield t[curr], None
        curr += 1

    while curr < len(k):
        yield None, k[curr]
        curr += 1


tutors_list = tutor_with_klass(tutors, klasses)
print(type(tutors_list))

for i in range (10):
    print(next(tutors_list))
