# Advent of Code 2015
# Day 7: Some Assembly Required
# Author: Dean Rumsby

from abc import ABC, abstractmethod

################################################################################
## Solutions
################################################################################


# This year, Santa brought little Bobby Tables a set of wires and bitwise
# logic gates! Unfortunately, little Bobby is a little under the recommended age
# range, and he needs help assembling the circuit.
#
# Each wire has an identifier (some lowercase letters) and can carry a 16-bit
# signal (a number from 0 to 65535). A signal is provided to each wire by a gate,
# another wire, or some specific value. Each wire can only get a signal from one
# source, but can provide its signal to multiple destinations. A gate provides no
# signal until all of its inputs have a signal.
#
# The included instructions booklet describes how to connect the parts together:
# x AND y -> z means to connect wires x and y to an AND gate, and then connect
# its output to wire z.
#
# For example:
#
# - 123 -> x means that the signal 123 is provided to wire x.
# - x AND y -> z means that the bitwise AND of wire x and wire y is provided
#   to wire z.
# - p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2
#   and then provided to wire q.
# - NOT e -> f means that the bitwise complement of the value from wire e
#   is provided to wire f.
#
# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift).
# If, for some reason, you'd like to emulate the circuit instead, almost all
# programming languages (for example, C, JavaScript, or Python) provide operators
# for these gates.
#
# For example, here is a simple circuit:
#
# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
#
# After it is run, these are the signals on the wires:
#
# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456
#
# In little Bobby's kit's instructions booklet (provided as your puzzle input), what
# signal is ultimately provided to wire a?
#
def part1():
    with open("example.txt", "r") as file:
        instructions = file.read().splitlines()

    for instruction in instructions:
        

    # return instructions


class CircuitComponent(ABC):
    def __init__(self):
        self.signal = 0
        self.child = None

    @abstractmethod
    def propagate(self):
        pass

    def update(self, signal):
        self.signal = signal

    def attach(self, component):
        self.child = component



class Source(CircuitComponent):
    def __init__(self, signal):
        super().__init__()
        self.signal = signal

    def propagate(self):
        if self.child:
            self.child.update(self.signal)


class Wire(CircuitComponent):
    def __init__(self):
        super().__init__()

    def propagate(self):
        if self.child:
            self.child.update(self.signal)


class AndGate(CircuitComponent):
    def __init__(self, source_a, source_b):
        super().__init__()
        self.a = source_a
        self.b = source_b

    def propagate(self):
        if self.child:
            self.child.update(self.a.signal & self.b.signal)


class OrGate(CircuitComponent):
    def __init__(self, source_a, source_b):
        super().__init__()
        self.a = source_a
        self.b = source_b

    def propagate(self):
        if self.child:
            self.child.update(self.a.signal | self.b.signal)


class NotGate(CircuitComponent):
    def __init__(self, source):
        super().__init__()
        self.a = source

    def propagate(self):
        if self.child:
            self.child.update(~(self.a.signal))


class LShiftGate(CircuitComponent):
    def __init__(self, source, shift):
        super().__init__()
        self.a = source
        self.shift = shift

    def signal(self):
        signal = self.a
        for _ in range(self.shift):
            signal <<= signal
        return signal


class RShiftGate(CircuitComponent):
    def __init__(self, source, shift):
        super().__init__()
        self.a = source
        self.shift = shift

    def signal(self):
        signal = self.a
        for _ in range(self.shift):
            signal >>= signal
        return signal


part1()
