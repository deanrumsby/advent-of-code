import re

with open("input.txt", "r") as file:
    strings = file.read().splitlines()


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


count = 0
for s in strings:
    if is_nice_string(s):
        count += 1

print(f"Part 1: There are {count} nice strings in the text file")
