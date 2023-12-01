with open("input.txt", "r") as file:
    instructions = file.read()


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


santa = Santa()

for instruction in instructions:
    santa.move(instruction)

unique_houses = santa.unique_locations()

print(f"Part 1: Santa delivered presents to {len(unique_houses)} different houses")

santa = Santa()
robo_santa = Santa()

for index, instruction in enumerate(instructions):
    if index % 2 == 0:
        santa.move(instruction)
    else:
        robo_santa.move(instruction)

unique_houses = santa.unique_locations().union(robo_santa.unique_locations())

print(
    f"Part 2: Santa and Robo Santa delivered presents to {len(unique_houses)} different houses"
)
