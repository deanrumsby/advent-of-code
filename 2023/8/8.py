import re
import time
from multiprocessing import Process, Queue

with open("input.txt", "r") as file:
    document = file.read()

instructions, network = document.split("\n\n")

nodes = {}

for node in network.split("\n"):
    name, left, right = re.findall(r"\w{3}", node)
    nodes[name] = (left, right)


def change_node(current_node, instruction):
    match instruction:
        case "L":
            return nodes[current_node][0]
        case "R":
            return nodes[current_node][1]
    raise Exception("Invalid instruction provided")


def get_instruction(steps):
    return instructions[steps % len(instructions)]


def worker(current_node, output):
    steps = 0
    while True:
        instruction = get_instruction(steps)
        current_node = change_node(current_node, instruction)

        if current_node[-1] == "Z":
            output.put(steps + 1)

        steps += 1


if __name__ == "__main__":
    # Part 1

    current_node = "AAA"
    steps = 0

    while current_node != "ZZZ":
        instruction = get_instruction(steps)
        current_node = change_node(current_node, instruction)
        steps += 1

    print(f"part 1: it takes {steps} steps to reach zzz")

    # current_nodes = [name for name in nodes.keys() if name[-1] == "a"]
    # steps = 0
    #
    # st = time.time()
    # # while any(name[-1] != "Z" for name in current_nodes):
    # while steps < 100000000:
    #     instruction = get_instruction(steps)
    #     current_nodes = [change_node(node, instruction) for node in current_nodes]
    #     steps += 1
    #
    # et = time.time()
    #
    # print(et - st)
    # Part 2

    st = time.time()
    current_nodes = [name for name in nodes.keys() if name[-1] == "A"]
    # outputs = [Queue() for _ in current_nodes]
    # processes = []
    #
    # for i in range(len(outputs)):
    #     p = Process(target=worker, args=(current_nodes[i], outputs[i]))
    #     p.start()
    #     processes.append(p)
    #
    # next_steps = [output.get() for output in outputs]
    # locked_index = 0
    # locked_steps = next_steps[locked_index]
    #
    # while next_steps.count(locked_steps) != len(next_steps):
    #     # while min(next_steps) < 100000000:
    #     new_next_steps = [0] * len(next_steps)
    #     for i, steps in enumerate(next_steps):
    #         if i == locked_index or steps == locked_steps:
    #             new_next_steps[i] = steps
    #
    #         if steps < locked_steps:
    #             new_next_steps[i] = outputs[i].get()
    #         else:
    #             locked_index = i
    #             locked_steps = steps
    #             new_next_steps[i] = steps
    #
    #     next_steps = new_next_steps
    #
    # for p in processes:
    #     p.terminate()
    #
    # et = time.time()
    #
    # print(et - st)
    # print(next_steps)
    print(current_nodes)

    node = "BGA"
    for i in range(10011408):
        instruction = get_instruction(i)
        node = change_node(node, instruction)

    print(node)

    # print(
    #     f"Part 2: It takes {next_steps[0]} steps to end up entirely on nodes that end in Z"
    # )
