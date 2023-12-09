import re

with open("input.txt", "r") as file:
    lines = file.read().splitlines()


def rank(hand, card_values, wildcard=None):
    no_wildcards_hand = hand.replace(wildcard, "") if wildcard else hand
    wildcard_count = hand.count(wildcard) if wildcard else 0

    repeated_cards = re.findall(r"(\w)(?=\w*(\1)\w*)", no_wildcards_hand)
    unique_repeated_cards_count = len(set(repeated_cards))

    if not unique_repeated_cards_count and wildcard_count > 0:
        unique_repeated_cards_count += 1

    repeated_card_count = min(
        len(repeated_cards) + unique_repeated_cards_count + wildcard_count, 5
    )

    hand_strength = 0  # high card
    match (repeated_card_count, unique_repeated_cards_count):
        case (5, 1):  # 5 of a kind
            hand_strength = 6
        case (4, 1):  # 4 of a kind
            hand_strength = 5
        case (5, 2):  # full house
            hand_strength = 4
        case (3, 1):  # 3 of a kind
            hand_strength = 3
        case (4, 2):  # 2 pairs
            hand_strength = 2
        case (2, 1):  # 1 pair
            hand_strength = 1

    numeric_hand = [
        int(card_values[card] if card_values.get(card) else card) for card in [*hand]
    ]  # converts eg AAJ42 to [14, 14, 11, 4, 2]

    # we will represent the hand as a base-13 number written in decimal
    hand_strength = hand_strength * (13**5)
    relative_hand_strength = 0
    for i, card_value in enumerate(numeric_hand):
        relative_hand_strength += card_value * (13 ** (4 - i))

    return hand_strength + relative_hand_strength


def calc_total_winnings(ranked_hands):
    total_winnings = 0
    for r, hand in enumerate(ranked_hands):
        (_, bid) = hand
        total_winnings += (r + 1) * bid
    return total_winnings


hands = []
for line in lines:
    hand, bid = line.split()
    hands.append((hand, int(bid)))


# Part 1

card_values = {"A": "14", "K": "13", "Q": "12", "J": "11", "T": "10"}
rank_hand = lambda h: rank(h[0], card_values)

ranked_hands = sorted(hands, key=rank_hand)

print(f"Part 1: The total winnings are {calc_total_winnings(ranked_hands)}")


# Part 2

card_values = {"A": "13", "K": "12", "Q": "11", "T": "10", "J": "1"}
rank_hand = lambda h: rank(h[0], card_values, "J")

ranked_hands = sorted(hands, key=rank_hand)

print(f"Part 2: The new total winnings are {calc_total_winnings(ranked_hands)}")
