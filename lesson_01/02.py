cubes_of_odd_numbers = list()
total = 0

for item in range(1, 1000):
    if item % 2 != 0:
        cubes_of_odd_numbers.append(item ** 3)

# print(f"Cubes of odd numbers:\n{cubes_of_odd_numbers}")

for cube in cubes_of_odd_numbers:
    sum_of_numbers_in_odd = 0
    for num in str(cube):
        sum_of_numbers_in_odd += int(num)
    if sum_of_numbers_in_odd % 7 == 0:
        total += sum_of_numbers_in_odd

print(f"Exercise A: {total}")

# 1st variant (expensive): prepare list for exercise "B"
# for cube in range(len(cubes_of_odd_numbers)):
#     cubes_of_odd_numbers[cube] += 17

# print(f"Cubes of odd numbers, increased by 17:\n{cubes_of_odd_numbers}")

for cube in cubes_of_odd_numbers:
    sum_of_numbers_in_odd = 0
    # 2nd variant (cheaper): add 17 for each element "in fly"
    for num in str(cube + 17):
        sum_of_numbers_in_odd += int(num)
    if sum_of_numbers_in_odd % 7 == 0:
        total += sum_of_numbers_in_odd

print(f"Exercise B: {total}")
