import re

with open("input.txt", "r") as file:
    lines = file.read().splitlines()


def find_adjacent_matches(pattern, location):
    i, (start_j, end_j) = location
    adjacent_span = set(range(start_j - 1, end_j + 1))

    is_out_of_bounds = lambda i: i < 0 or i >= len(lines)
    is_adjacent = lambda m: not adjacent_span.isdisjoint(set(range(m.start(), m.end())))

    adjacent_matches = []

    for di in [-1, 0, 1]:
        i_bar = i + di

        if is_out_of_bounds(i_bar):
            continue

        matches = re.finditer(pattern, lines[i_bar])
        adjacent_matches.extend(list(filter(is_adjacent, matches)))

    return adjacent_matches


part_numbers_sum = 0
gear_ratio_sum = 0

for i, line in enumerate(lines):
    numbers = re.finditer(r"\d+", line)
    potential_gears = re.finditer(r"\*", line)

    for number in numbers:
        adjacent_symbols = find_adjacent_matches(r"[^\.\d]", (i, number.span()))

        if adjacent_symbols:
            part_numbers_sum += int(number.group())

    for pg in potential_gears:
        adjacent_numbers = find_adjacent_matches(r"\d+", (i, pg.span()))

        if len(adjacent_numbers) == 2:
            gear_ratio = 1
            for an in adjacent_numbers:
                gear_ratio *= int(an.group())

            gear_ratio_sum += gear_ratio


print(f"Part 1: The sum of all the part numbers is {part_numbers_sum}")
print(f"Part 2: The sum of all the gear ratios is {gear_ratio_sum}")
