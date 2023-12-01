import re

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

# Part 1
total = 0

for line in lines:
    digits = re.findall(r"\d", line)
    calibration_value = int(f"{digits[0]}{digits[-1]}")
    total += calibration_value

print(f"Part 1: The sum of all the calibration values is {total}")

# Part 2

number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replace_worded_number(s):
    if number_map.get(s):
        return number_map[s]
    return s


new_total = 0

for line in lines:
    mixed_digits = re.findall(
        r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line
    )  # using capture group inside positive lookahead regex pattern to collect overlapping matches
    digits = list(map(replace_worded_number, mixed_digits))
    calibration_value = int(f"{digits[0]}{digits[-1]}")
    new_total += calibration_value

print(f"Part 2: The sum of all the new calibration values is {new_total}")
