class Range:
    def __init__(self, start, length):
        self.start = start
        self.end = start + length - 1
        self.length = length

    def includes(self, r: "Range"):
        return self.start <= r.start and self.end >= r.end

    def partition(self, points: list[int]):
        parts = []
        current = self
        for point in sorted(points):
            if point <= current.start or point > current.end:
                continue
            parts.append(Range(current.start, point - current.start))
            current = Range(point, current.end - point + 1)
        parts.append(current)
        return parts


class Map:
    def __init__(self, domain: list[Range], image: list[Range]):
        self.domain = domain
        self.image = image

    def map(self, ranges: list[Range]):
        outputs = []
        for r in ranges:
            outputs.extend(self.__map(r))
        return outputs

    def __map(self, range_: Range):
        partition_points = []
        outputs = []

        for domain_range in self.domain:
            partition_points.extend([domain_range.start, domain_range.end + 1])

        parts = range_.partition(partition_points)

        for part in parts:
            for i, domain_range in enumerate(self.domain):
                if not domain_range.includes(part):
                    continue
                offset = part.start - domain_range.start
                mapped_start = self.image[i].start + offset
                length = part.length
                outputs.append(Range(mapped_start, length))
                break
            else:
                outputs.append(part)

        return outputs


with open("input.txt", "r") as file:
    almanac = file.read().split("\n\n")

seeds_section, maps_section = almanac[0], almanac[1:]

maps = {}


for map_text in maps_section:
    lines = map_text.split("\n")

    map_name = lines[0].split()[0]

    mapping_data = [
        [int(value) for value in mapping_string.split()] for mapping_string in lines[1:]
    ]

    domain = []
    image = []
    for dest, source, length in mapping_data:
        domain.append(Range(source, length))
        image.append(Range(dest, length))

    maps[map_name] = Map(domain, image)


def seed_to_location(range_: Range):
    outputs = [range_]
    for map_name in [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]:
        outputs = maps[map_name].map(outputs)
    return outputs


seeds_data = [int(seed_string) for seed_string in seeds_section[7:].split()]


# Part 1

single_seeds = [Range(value, 1) for value in seeds_data]

location_numbers = []

for seed_data in single_seeds:
    location_range = seed_to_location(seed_data)
    location_numbers.append(location_range[0].start)

print(f"Part 1: The lowest location number is {min(location_numbers)}")


# Part 2

ranged_seeds = [
    Range(seed, length) for seed, length in zip(seeds_data[::2], seeds_data[1::2])
]

all_location_ranges = []

for seed_data in ranged_seeds:
    location_ranges = seed_to_location(seed_data)
    all_location_ranges.extend(location_ranges)

minimal_location_numbers = [
    location_range.start for location_range in all_location_ranges
]

print(f"Part 2: The new lowest location number is {min(minimal_location_numbers)}")
