# Day 2: I Was Told There Would Be No Math

[Question Page](https://adventofcode.com/2015/day/2)

Solution by Dean Rumsby

## Part 1

We are going to loop over each set of dimensions provided by the given input data.
That way we can calculate the wrapping paper needed for each present and add it to a
running total.

Lets start by reading our data into a list, so that we can iterate over it easily.

```python
with open("input.txt", "r") as file:
    dimensions = file.read().splitlines()
```

Our running total can be initialized too.

```python
wrapping_paper = 0
```

Now, when we iterate we will need to calculate the surface area and smallest side area
of each box. I think it makes sense to create a function for each of these calculations.

```python
def calc_surface_area(l: int, w: int, h: int) -> int:
    return (2 * l* w) + (2 * l * h) + (2 * w * h)

def calc_smallest_side_area(l: int, w: int, h: int) -> int:
    return min(l * w, l * h, w * h)
```

We need to take care when we loop over the data, to ensure we parse it correctly. We have to split the
strings and type cast each separate dimension from string to integer (unless we change our function
signatures). I use a combination of unpacking and [generator expressions](https://peps.python.org/pep-0289/)
to accomplish this cleanly, in Python.

```python
for dims in dimensions:
    l, w, h = (int(d) for d in dims.split("x"))
    surface_area = calc_surface_area(l, w, h)
    smallest_side_area = calc_smallest_side_area(l, w, h)
    wrapping_paper += surface_area + smallest_side_area
```

So our solution for part 1 looks like

```python
def part1() -> int:
    with open("input.txt", "r") as file:
        dimensions = file.read().splitlines()

    wrapping_paper = 0

    for dims in dimensions:
        l, w, h = (int(d) for d in dims.split("x"))
        surface_area = calc_surface_area(l, w, h)
        smallest_side_area = calc_smallest_side_area(l, w, h)
        wrapping_paper += surface_area + smallest_side_area

    return wrapping_paper

```
