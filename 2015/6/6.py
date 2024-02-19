# Advent of Code 2015
# Day 6: Probably a Fire Hazard
# Author: Dean Rumsby

import re


# Because your neighbors keep defeating you in the holiday house decorating
# contest year after year, you've decided to deploy one million lights in a
# 1000x1000 grid.
#
# Furthermore, because you've been especially nice this year, Santa has
# mailed you instructions on how to display the ideal lighting configuration.
#
# Lights in your grid are numbered from 0 to 999 in each direction; the lights
# at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions
# include whether to turn on, turn off, or toggle various inclusive ranges
# given as coordinate pairs. Each coordinate pair represents opposite corners
# of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore
# refers to 9 lights in a 3x3 square. The lights all start turned off.
#
# To defeat your neighbors this year, all you have to do is set up your lights
# by doing the instructions Santa sent you in order.
#
# For example:
#
# - turn on 0,0 through 999,999 would turn on (or leave on) every light.
# - toggle 0,0 through 999,0 would toggle the first line of 1000 lights,
#   turning off the ones that were on, and turning on the ones that were off.
# - turn off 499,499 through 500,500 would turn off (or leave off) the middle
#   four lights.
#
# After following the instructions, how many lights are lit?
#
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


# You just finish implementing your winning light pattern when you realize you
# mistranslated Santa's message from Ancient Nordic Elvish.
#
# The light grid you bought actually has individual brightness controls; each
# light can have a brightness of zero or more. The lights all start at zero.
#
# The phrase turn on actually means that you should increase the brightness of
# those lights by 1.
#
# The phrase turn off actually means that you should decrease the brightness of
# those lights by 1, to a minimum of zero.
#
# The phrase toggle actually means that you should increase the brightness of
# those lights by 2.
#
# What is the total brightness of all lights combined after following Santa's
# instructions?
#
# For example:
#
# - turn on 0,0 through 0,0 would increase the total brightness by 1.
# - toggle 0,0 through 999,999 would increase the total brightness by 2000000.
#
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


# Shared classes


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


# Print solutions

print(f"Part 1: There are {part1()} lights lit after following the instructions")
print(f"Part 2: The total brightness is {part2()} after following the instructions")
