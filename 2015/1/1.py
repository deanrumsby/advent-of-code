# Advent of Code 2015
# Day 1: Not Quite Lisp
# Author: Dean Rumsby

################################################################################
## Solutions
################################################################################


# Santa is trying to deliver presents in a large apartment building, but he
# can't find the right floor - the directions he got are a little confusing. He
# starts on the ground floor (floor 0) and then follows the instructions one
# character at a time.
#
# An opening parenthesis, (, means he should go up one floor, and a closing
# parenthesis, ), means he should go down one floor.
#
# The apartment building is very tall, and the basement is very deep; he will
# never find the top or bottom floors.
#
# For example:
#
# - (()) and ()() both result in floor 0.
# - ((( and (()(()( both result in floor 3.
# - ))((((( also results in floor 3.
# - ()) and ))( both result in floor -1 (the first basement level).
# - ))) and )())()) both result in floor -3.
#
# To what floor do the instructions take Santa?
#
def part1() -> int:
    with open("input.txt", "r") as file:
        instructions = file.read()

    floor = 0

    for instruction in instructions:
        floor = change_floor(floor, instruction)

    return floor


# Now, given the same instructions, find the position of the first character
# that causes him to enter the basement (floor -1). The first character in the
# instructions has position 1, the second character has position 2, and so on.
#
# For example:
#
# - ) causes him to enter the basement at character position 1.
# - ()()) causes him to enter the basement at character position 5.
#
# What is the position of the character that causes Santa to first enter
# the basement?
#
def part2() -> int | None:
    with open("input.txt", "r") as file:
        instructions = file.read()

    floor = 0
    BASEMENT = -1

    for index, instruction in enumerate(instructions):
        floor = change_floor(floor, instruction)

        if floor == BASEMENT:
            return index + 1

    return None


################################################################################
## Global functions
################################################################################


def change_floor(floor: int, instruction: str) -> int:
    match instruction:
        case "(":
            return floor + 1
        case ")":
            return floor - 1
        case _:
            return floor


################################################################################
## Answers
################################################################################

print(f"Part 1: Santa is directed to floor {part1()}")
print(f"Part 2: Santa first enters the basement at position {part2()}")
