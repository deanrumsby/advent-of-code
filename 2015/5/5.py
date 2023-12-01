import re

with open("input.txt", "r") as file:
    strings = file.read().splitlines()

# Part 1


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

# Part 2


def does_contain_pair_twice(s):
    return bool(re.search(r"(\w\w).*(\1)", s))


def does_contain_repeat_with_letter_between(s):
    return bool(re.search(r"(\w)\w(\1)", s))


def is_nicer_string(s):
    return bool(
        does_contain_pair_twice(s) and does_contain_repeat_with_letter_between(s)
    )


new_count = 0
for s in strings:
    if is_nicer_string(s):
        new_count += 1

print(f"Part 2: There are {new_count} nice strings with regard to the new rules")
