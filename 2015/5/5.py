# Advent of Code 2015
# Day 5

import re


# How many strings are nice?
def part1():
    def does_contain_three_vowels(s):
        return bool(re.search(r"(.*(a|e|i|o|u).*){3}", s))

    def does_contain_a_double_letter(s):
        return bool(re.search(r"(\w)\1", s))

    def does_contain_illegal_substring(s):
        return bool(re.search(r"(ab|cd|pq|xy)", s))

    def is_nice_string(s):
        return bool(
            does_contain_three_vowels(s)
            and does_contain_a_double_letter(s)
            and not does_contain_illegal_substring(s)
        )

    with open("input.txt", "r") as file:
        strings = file.read().splitlines()

    count = 0

    for s in strings:
        if is_nice_string(s):
            count += 1

    return count


# How many strings are nice under these new rules?
def part2():
    def does_contain_pair_twice(s):
        return bool(re.search(r"(\w\w).*(\1)", s))

    def does_contain_repeat_with_letter_between(s):
        return bool(re.search(r"(\w)\w(\1)", s))

    def is_nice_string(s):
        return bool(
            does_contain_pair_twice(s) and does_contain_repeat_with_letter_between(s)
        )

    with open("input.txt", "r") as file:
        strings = file.read().splitlines()

    count = 0

    for s in strings:
        if is_nice_string(s):
            count += 1

    return count


print(f"Part 1: There are {part1()} nice strings in the text file")
print(f"Part 2: There are {part2()} nice strings with regard to the new rules")
