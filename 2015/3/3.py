# Advent of Code 2015
# Day 3


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


# How many houses receive at least one present?
def part1():
    with open("input.txt", "r") as file:
        instructions = file.read()

    santa = Santa()
    for instruction in instructions:
        santa.move(instruction)

    unique_houses = santa.unique_locations()

    return len(unique_houses)


# This year, how many houses receive at least one present?
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


print(f"Part 1: Santa delivered presents to {part1()} different houses")
print(f"Part 2: Santa and Robo Santa delivered presents to {part2()} different houses")
