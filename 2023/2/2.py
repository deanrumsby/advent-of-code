import re

with open("input.txt", "r") as file:
    games = file.read().splitlines()

id_sum = 0
power_sum = 0

for game in games:
    id = int(re.findall(r"(?<=Game )\d+", game)[0])
    blues = list(map(int, re.findall(r"\d+(?= blue)", game)))
    reds = list(map(int, re.findall(r"\d+(?= red)", game)))
    greens = list(map(int, re.findall(r"\d+(?= green)", game)))

    max_blue = max(blues)
    max_red = max(reds)
    max_green = max(greens)

    if max_red <= 12 and max_green <= 13 and max_blue <= 14:
        id_sum += id

    power = max_blue * max_red * max_green
    power_sum += power

print(f"Part 1: The sum of the IDs of all possible games is {id_sum}")
print(f"Part 2: The sum of the powers of the minimal sets is {power_sum}")
