import re

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

DIRECTIONS = [
    (1, 1),
    (1, 0),
    (1, -1),
    (0, 1),
    (0, -1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
]


class EngineEntity:
    def __init__(self, id, coords):
        self.id = id
        self.coords = coords


class EngineNumber(EngineEntity):
    def __init__(self, id, coords, value):
        super().__init__(id, coords)
        self.value = value


class EngineSymbol(EngineEntity):
    def __init__(self, id, coords, symbol):
        super().__init__(id, coords)
        self.symbol = symbol


class EngineMap:
    def __init__(self):
        self.map = {}

    def add(self, entity):
        for i, j in entity.coords:
            self.map[(i, j)] = entity

    def adjacent(self, entity):
        entities = []

        for i, j in entity.coords:
            for di, dj in DIRECTIONS:
                i_bar = i + di
                j_bar = j + dj

                if (i_bar, j_bar) in entity.coords:
                    continue
                if not self.map.get((i_bar, j_bar)):
                    continue

                adjacent_entity = self.map[(i_bar, j_bar)]

                if any(obj.id == adjacent_entity.id for obj in entities):
                    continue

                entities.append(adjacent_entity)

        return entities

    def is_adjacent_to_symbol(self, entity):
        return any(isinstance(obj, EngineSymbol) for obj in self.adjacent(entity))

    def adjacent_numbers(self, entity):
        return list(
            filter(lambda obj: isinstance(obj, EngineNumber), self.adjacent(entity))
        )


entity_count = 0
engine_numbers = []
engine_symbols = []
engine_map = EngineMap()

# parsing the schematics
for i, line in enumerate(lines):
    numbers = re.finditer(r"\d+", line)
    symbols = re.finditer(r"[^\d\.]", line)

    # creating EngineNumber objects
    for number in numbers:
        coords = [(i, j) for j in range(number.start(), number.end())]
        engine_number = EngineNumber(entity_count, coords, int(number.group()))
        engine_map.add(engine_number)
        engine_numbers.append(engine_number)
        entity_count += 1

    # creating EngineSymbol objects
    for symbol in symbols:
        coords = [(i, symbol.start())]
        engine_symbol = EngineSymbol(entity_count, coords, symbol.group())
        engine_map.add(engine_symbol)
        engine_symbols.append(engine_symbol)
        entity_count += 1


part_numbers_sum = 0
for number in engine_numbers:
    if engine_map.is_adjacent_to_symbol(number):
        part_numbers_sum += number.value

gear_ratio_sum = 0
for symbol in engine_symbols:
    if symbol.symbol != "*":
        continue

    adjacent_numbers = engine_map.adjacent_numbers(symbol)
    if len(adjacent_numbers) == 2:
        gear_ratio = 1
        for number in adjacent_numbers:
            gear_ratio *= number.value
        gear_ratio_sum += gear_ratio

print(f"Part 1: The sum of all the part numbers is {part_numbers_sum}")
print(f"Part 2: The sum of all the gear ratios is {gear_ratio_sum}")
