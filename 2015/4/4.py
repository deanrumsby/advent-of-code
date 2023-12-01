import hashlib

SECRET_KEY = "yzbqklnj"


def mine(difficulty):
    nonce = 0

    while True:
        message = f"{SECRET_KEY}{nonce}".encode()
        hash = hashlib.md5(message).hexdigest()

        if hash[:difficulty] == "0" * difficulty:
            return nonce

        nonce += 1


print(f"Part 1: The nonce required to mine the first AdventCoin is {mine(5)}")
print(f"Part 2: The nonce required to mine the second AdventCoin is {mine(6)}")
