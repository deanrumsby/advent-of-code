# Advent of Code 2015
# Day 4: The Ideal Stocking Stuffer
# Author: Dean Rumsby

import hashlib

################################################################################
## Solutions
################################################################################

SECRET_KEY = "yzbqklnj"


# Santa needs help mining some AdventCoins (very similar to bitcoins) to use as
# gifts for all the economically forward-thinking little girls and boys.
#
# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at
# least five zeroes. The input to the MD5 hash is some secret key
# (your puzzle input, given below) followed by a number in decimal. To mine
# AdventCoins, you must find Santa the lowest positive number
# (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
#
# For example:
#
# - If your secret key is abcdef, the answer is 609043, because the MD5 hash of
#   abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest
#   such number to do so.
# - If your secret key is pqrstuv, the lowest number it combines with to make
#   an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of
#   pqrstuv1048970 looks like 000006136ef....
#
def part1():
    return mine(SECRET_KEY, 5)


# Now find one that starts with six zeroes.
#
def part2():
    return mine(SECRET_KEY, 6)


################################################################################
## Shared functions
################################################################################


def mine(key, difficulty):
    nonce = 0

    while True:
        message = f"{key}{nonce}".encode()
        hash = hashlib.md5(message).hexdigest()

        if hash[:difficulty] == "0" * difficulty:
            return nonce

        nonce += 1


################################################################################
## Print answers
################################################################################

print(f"Part 1: The nonce required to mine the first AdventCoin is {part1()}")
print(f"Part 2: The nonce required to mine the second AdventCoin is {part2()}")
