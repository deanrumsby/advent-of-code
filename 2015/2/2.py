with open("input.txt") as file:
    dimensions = file.read().splitlines()


class Box:
    def __init__(self, width, length, height):
        self.w = width
        self.l = length
        self.h = height

    def surface_area(self):
        return (2 * self.w * self.h) + (2 * self.w * self.l) + (2 * self.h * self.l)

    def volume(self):
        return self.w * self.l * self.h

    def smallest_side(self):
        return min(self.w * self.h, self.w * self.l, self.h * self.l)

    def smallest_perimeter(self):
        return min(2 * (self.w + self.h), 2 * (self.w + self.l), 2 * (self.h + self.l))


def calc_wrapping_paper_needed(box):
    return box.surface_area() + box.smallest_side()


def calc_ribbon_needed(box):
    return box.volume() + box.smallest_perimeter()


wrapping_paper = 0
ribbon = 0

for d in dimensions:
    w, l, h = [
        int(x) for x in d.split("x")
    ]  # converts a string "2x3x4" into a list of ints [2, 3, 4]
    box = Box(w, l, h)
    wrapping_paper += calc_wrapping_paper_needed(box)
    ribbon += calc_ribbon_needed(box)

print(f"Part 1: The elves need to order {wrapping_paper} square feet of wrapping paper")
print(f"Part 2: The elves need to order {ribbon} feet of ribbon")
