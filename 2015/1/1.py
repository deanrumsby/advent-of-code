with open("input.txt", "r") as file:
    directions = file.read()


def change_floor(floor, direction):
    match direction:
        case "(":
            return floor + 1
        case ")":
            return floor - 1
        case _:
            return floor


BASEMENT = -1
floor = 0
basement_position = None


for index, direction in enumerate(directions):
    floor = change_floor(floor, direction)

    if basement_position == None and floor == BASEMENT:
        basement_position = index + 1


print(f"Part 1: Santa is directed to floor {floor}")
print(f"Part 2: Santa first enters the basement at position {basement_position}")
