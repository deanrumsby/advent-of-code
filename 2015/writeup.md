# Advent of Code 2015

## Day 1: Not Quite Lisp

[Question Page](https://adventofcode.com/2015/day/1)

Solution by Dean Rumsby

### Part 1

I think that the natural solution to this problem is to process each instruction in sequence,
and to see what floor we arrive at.

We are told that Santa starts on floor 0 of the apartment building, so let's start by
initializing a variable to keep track of the floor he is on.

```
floor = 0
```

Next, we need to create a function that can compute the next floor value, given an instruction.
I prefer to keep my functions [pure](https://en.wikipedia.org/wiki/Pure_function) where possible,
so I will also pass in the current floor value.

```
def change_floor(floor, instruction):
    match instruction:
        case "(":
            return floor + 1
        case ")":
            return floor - 1
        case _:
            return floor
```

Let's read in our instructions now so that we can process them.

```
with open("input.txt", "r") as file:
    instructions = file.read()
```

To process each instruction we will need to use a loop.

```
for instruction in instructions:
    floor = change_floor(floor, instruction)
```

Once the instructions have been processed we can print our answer.

```
print(f"Part 1: Santa is directed to floor {floor}")
```
