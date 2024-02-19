# Advent of Code 2015
# Day 6

import re


class Instruction:
    def __init__(self, action: str, start: tuple[int, int], end: tuple[int, int]):
        self.action = action
        self.start = start
        self.end = end

    @classmethod
    def from_instruction_string(cls, instruction_string):
        action = re.findall(r"turn on|turn off|toggle", instruction_string)[0]
        coords = re.findall(r"\d+,\d+", instruction_string)
        start = tuple(map(int, coords[0].split(",")))
        end = tuple(map(int, coords[1].split(",")))
        return cls(action, start, end)


class LightGrid:
    def __init__(self, width, height):
        self.lights = [[0] * width for _ in range(height)]

    def subgrid(self, start, end):
        return SubGrid(self, start, end)

    def on_count(self):
        count = 0
        for row in self.lights:
            count += len(row) - row.count(0)
        return count

    def total_brightness(self):
        total = 0
        for row in self.lights:
            total += sum(row)
        return total


class SubGrid:
    def __init__(self, lightgrid, start, end):
        self.parent = lightgrid
        self.start = start
        self.end = end

    def turn_on(self):
        self.__apply(lambda _: 1)

    def turn_off(self):
        self.__apply(lambda _: 0)

    def toggle(self):
        self.__apply(lambda x: 1 if x == 0 else 0)

    def increase(self, amount):
        self.__apply(lambda x: x + amount)

    def decrease(self, amount):
        self.__apply(lambda x: x - amount if x - amount >= 0 else 0)

    def __apply(self, func):
        (x1, y1) = self.start
        (x2, y2) = self.end
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.parent.lights[x][y] = func(self.parent.lights[x][y])


# After following the instructions, how many lights are lit?
def part1():
    with open("input.txt", "r") as file:
        instruction_strings = file.read().splitlines()

    lights = LightGrid(1000, 1000)

    for ins_string in instruction_strings:
        instruction = Instruction.from_instruction_string(ins_string)
        (start, end) = [instruction.start, instruction.end]

        match instruction.action:
            case "turn on":
                lights.subgrid(start, end).turn_on()
            case "turn off":
                lights.subgrid(start, end).turn_off()
            case "toggle":
                lights.subgrid(start, end).toggle()

    return lights.on_count()


# What is the total brightness of all lights combined after following
# Santa's instructions?
def part2():
    with open("input.txt", "r") as file:
        instruction_strings = file.read().splitlines()

    lights = LightGrid(1000, 1000)

    for ins_string in instruction_strings:
        instruction = Instruction.from_instruction_string(ins_string)
        (start, end) = [instruction.start, instruction.end]

        match instruction.action:
            case "turn on":
                lights.subgrid(start, end).increase(1)
            case "turn off":
                lights.subgrid(start, end).decrease(1)
            case "toggle":
                lights.subgrid(start, end).increase(2)

    return lights.total_brightness()


print(f"Part 1: There are {part1()} lights lit after following the instructions")
print(f"Part 2: The total brightness is {part2()} after following the instructions")
