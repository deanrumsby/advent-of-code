# Advent of Code 2015
# Day 3: Perfectly Spherical Houses in a Vacuum
# Author: Dean Rumsby

################################################################################
## Solutions
################################################################################


# Santa is delivering presents to an infinite two-dimensional grid of houses.
#
# He begins by delivering a present to the house at his starting location, and
# then an elf at the North Pole calls him via radio and tells him where to
# move next. Moves are always exactly one house to the north (^), south (v),
# east (>), or west (<). After each move, he delivers another present to the
# house at his new location.
#
# However, the elf back at the north pole has had a little too much eggnog, and
# so his directions are a little off, and Santa ends up visiting some houses more
# than once. How many houses receive at least one present?
#
# For example:
#
# - > delivers presents to 2 houses: one at the starting location, and one to
#   the east.
# - ^>v< delivers presents to 4 houses in a square, including twice to the house
#   at his starting/ending location.
# - ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only
#   2 houses.
#
# How many houses receive at least one present?
#
def part1():
    with open("input.txt", "r") as file:
        instructions = file.read()

    santa = Santa()
    for instruction in instructions:
        santa.move(instruction)

    unique_houses = santa.unique_locations()

    return len(unique_houses)


# The next year, to speed up the process, Santa creates a robot version of
# himself, Robo-Santa, to deliver presents with him.
#
# Santa and Robo-Santa start at the same location (delivering two presents to the
# same starting house), then take turns moving based on instructions from the
# elf, who is eggnoggedly reading from the same script as the previous year.
#
# This year, how many houses receive at least one present?
#
# For example:
#
# - ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa
#   goes south.
# - ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back
#   where they started.
# - ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and
#   Robo-Santa going the other.
#
def part2():
    with open("input.txt", "r") as file:
        instructions = file.read()

    santa = Santa()
    robo_santa = Santa()
    should_move_santa = True

    for instruction in instructions:
        if should_move_santa:
            santa.move(instruction)
        else:
            robo_santa.move(instruction)
        should_move_santa = not should_move_santa

    unique_houses = santa.unique_locations().union(robo_santa.unique_locations())

    return len(unique_houses)


################################################################################
## Shared classes
################################################################################


class Santa:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.history = []

        self.history.append((self.x, self.y))

    def move(self, instruction):
        match instruction:
            case "^":
                self.y += 1
            case ">":
                self.x += 1
            case "v":
                self.y -= 1
            case "<":
                self.x -= 1

        self.history.append((self.x, self.y))

    def unique_locations(self):
        return set(self.history)


################################################################################
## Print answers
################################################################################

print(f"Part 1: Santa delivered presents to {part1()} different houses")
print(f"Part 2: Santa and Robo Santa delivered presents to {part2()} different houses")
