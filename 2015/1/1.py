# Advent of Code 2015
# Day 1


def change_floor(floor, direction):
    match direction:
        case "(":
            return floor + 1
        case ")":
            return floor - 1
        case _:
            return floor


# To what floor do the instructions take Santa?
def part1():
    with open("input.txt", "r") as file:
        directions = file.read()

    floor = 0

    for direction in directions:
        floor = change_floor(floor, direction)

    return floor


# What is the position of the character that causes Santa to first enter the
# basement?
def part2():
    with open("input.txt", "r") as file:
        directions = file.read()

    floor = 0
    BASEMENT = -1

    for index, direction in enumerate(directions):
        floor = change_floor(floor, direction)

        if floor == BASEMENT:
            return index + 1

    return None


print(f"Part 1: Santa is directed to floor {part1()}")
print(f"Part 2: Santa first enters the basement at position {part2()}")
