# Advent of Code 2015
# Day 2


class Box:
    def __init__(self, width, length, height):
        self.w = width
        self.l = length
        self.h = height

    @classmethod
    def from_string(cls, dims_as_string):
        w, l, h = [int(x) for x in dims_as_string.split("x")]
        return cls(w, l, h)

    def surface_area(self):
        return (2 * self.w * self.h) + (2 * self.w * self.l) + (2 * self.h * self.l)

    def volume(self):
        return self.w * self.l * self.h

    def smallest_side(self):
        return min(self.w * self.h, self.w * self.l, self.h * self.l)

    def smallest_perimeter(self):
        return min(2 * (self.w + self.h), 2 * (self.w + self.l), 2 * (self.h + self.l))


# How many total square feet of wrapping paper should they order?
def part1():
    def calc_wrapping_paper_needed(box):
        return box.surface_area() + box.smallest_side()

    with open("input.txt") as file:
        dimensions = file.read().splitlines()

    wrapping_paper = 0

    for dims in dimensions:
        box = Box.from_string(dims)
        wrapping_paper += calc_wrapping_paper_needed(box)

    return wrapping_paper


# How many total feet of ribbon should they order?
def part2():
    def calc_ribbon_needed(box):
        return box.volume() + box.smallest_perimeter()

    with open("input.txt") as file:
        dimensions = file.read().splitlines()

    ribbon = 0

    for dims in dimensions:
        box = Box.from_string(dims)
        ribbon += calc_ribbon_needed(box)

    return ribbon


print(f"Part 1: The elves need to order {part1()} square feet of wrapping paper")
print(f"Part 2: The elves need to order {part2()} feet of ribbon")
