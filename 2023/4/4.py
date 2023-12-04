with open("input.txt", "r") as file:
    cards = file.read().splitlines()


total_points = 0

card_counts = {id: 1 for id in range(len(cards))}
total_cards = 0

for id, card in enumerate(cards):
    player_numbers, winning_numbers = list(
        map(lambda s: [int(char) for char in s.split()], card[9:].split("|"))
    )

    # Part 1
    winning = 0
    for pn in player_numbers:
        if pn in winning_numbers:
            winning += 1

    total_points += 2 ** (winning - 1) if winning else 0

    # Part 2
    for _ in range(card_counts[id]):
        for i in range(1, winning + 1):
            card_counts[id + i] += 1

    total_cards += card_counts[id]


print(f"Part 1: The scratchcards are worth {total_points} points in total")
print(f"Part 2: We end up with {total_cards} scratchcards in total")
