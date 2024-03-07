# Day 1: Trebuchet?!

[Question Page](https://adventofcode.com/2023/day/1)

Solution by Dean Rumsby

## Part 1

We are looking to extract the digits from each line of our input, which is
essentially a task of pattern matching and parsing data from strings.
Whenever I have to parse strings I will often reach for regular expressions
to accomplish this cleanly, so that is what I will use here too.

```python
import re
```

Before we can process anything we need to load the input data into memory, so
let's do that.

```python
with open("input.txt", "r") as file:
    lines = file.read().splitlines()
```

And we can initialize a variable to track the running total of our 'calibration
values'

```python
total = 0
```

We can compile a regular expression pattern that will match on the numerals
within the string.

```python
pattern = re.compile(r"\d")
```

Now we can loop over each line, collecting an array of all the digits.
Once we have the digits we can concatenate the first and last as a string,
and then typecast the result into an integer value. This is our calibration
value, which we can then add to the running total.

```python
for line in lines:
    digits = pattern.findall(line)
    calibration_value = int(f"{digits[0]}{digits[-1]}")
    total += calibration_value
```

This can be all combined into a neat function for returning the answer to part 1.

```python
def part1() -> int:
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    total = 0
    pattern = re.compile(r"\d")

    for line in lines:
        digits = pattern.findall(line)
        calibration_value = int(f"{digits[0]}{digits[-1]}")
        total += calibration_value

    return total
```
