# Advent of Code 2015
# Day 4

import hashlib

SECRET_KEY = "yzbqklnj"


def mine(key, difficulty):
    nonce = 0

    while True:
        message = f"{key}{nonce}".encode()
        hash = hashlib.md5(message).hexdigest()

        if hash[:difficulty] == "0" * difficulty:
            return nonce

        nonce += 1


# To mine AdventCoins, you must find Santa the lowest positive number that
# produces such a hash (a hash that starts with at least five leading zeroes)
def part1():
    return mine(SECRET_KEY, 5)


# Now find one that starts with six zeroes.
def part2():
    return mine(SECRET_KEY, 6)


print(f"Part 1: The nonce required to mine the first AdventCoin is {part1()}")
print(f"Part 2: The nonce required to mine the second AdventCoin is {part2()}")
