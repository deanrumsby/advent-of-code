with open("input.txt", "r") as file:
    stats = file.read().splitlines()

times: list[str] = stats[0].split()[1:]
best_distances: list[str] = stats[1].split()[1:]


def determine_winning_methods_count(time, best_distance):
    winning_methods_count = 0
    for button_hold_time in range(time):
        speed = button_hold_time
        time_to_move = time - button_hold_time
        distance = speed * time_to_move

        if distance > best_distance:
            winning_methods_count += 1

    return winning_methods_count


# Part 1

races = [
    (int(time), int(best_distance))
    for (time, best_distance) in zip(times, best_distances)
]

winning_method_product = 1

for time, best_distance in races:
    winning_method_product *= determine_winning_methods_count(time, best_distance)

print(
    f"Part 1: You get {winning_method_product} when you multiply together the number of ways you can beat each record"
)


# Part 2

time = int("".join(times))
best_distance = int("".join(best_distances))

winning_methods_count = determine_winning_methods_count(time, best_distance)

print(f"Part 2: There are {winning_methods_count} ways of beating the longer race")
