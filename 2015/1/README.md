# Day 1: Not Quite Lisp

[Question Page](https://adventofcode.com/2015/day/1)

Solution by Dean Rumsby

## Part 1

I think that the natural solution to this problem is to process each instruction in sequence,
and to see what floor we arrive at.

We are told that Santa starts on floor 0 of the apartment building, so let's start by
initializing a variable to keep track of the floor he is on.

```python
floor = 0
```

Next, we need to create a function that can compute the next floor value, given an instruction.
I prefer to keep my functions [pure](https://en.wikipedia.org/wiki/Pure_function) where possible,
so I will also pass in the current floor value.

```python
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

```python
with open("input.txt", "r") as file:
    instructions = file.read()
```

To process each instruction we will need to use a loop.

```python
for instruction in instructions:
    floor = change_floor(floor, instruction)
```

Putting it all together gives us a function that returns the answer for part 1.

```python
def part1():
    with open("input.txt", "r") as file:
        instructions = file.read()

    floor = 0

    for instruction in instructions:
        floor = change_floor(floor, instruction)

    return floor
```

## Part 2

Again, keeping things simple, let's process each instruction until we first enter the basement.
We only need to modify the code of our loop, using `enumerate` to give us access to the index of
each instruction, and a conditional to see if we have entered the basement.

```python
BASEMENT = -1

for index, instruction in enumerate(instructions):
    floor = change_floor(floor, instruction)

    if floor == BASEMENT:
        return index + 1
```

All the rest of the code remains the same. In both parts we use the `change_floor` function from part 1, which is why
it is so useful to keep functions pure.

So our solution for part 2 looks like...

```python
def part2():
    with open("input.txt", "r") as file:
        instructions = file.read()

    floor = 0
    BASEMENT = -1

    for index, instruction in enumerate(instructions):
        floor = change_floor(floor, instruction)

        if floor == BASEMENT:
            return index + 1

    return None
```
