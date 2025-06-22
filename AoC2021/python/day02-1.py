#!/bin/env python
# Advent of Code 2021 Day 2 first
# from python.utils import read_file


def exec_commands(commands):
    pos = depth = 0
    for c,val in commands:
        if c == 'forward':
            pos += int(val)
        elif c == 'up':
            depth -= int(val)
        elif c == 'down':
            depth += int(val)
    return pos, depth


def read_file(filename:str) -> list:
    with open(filename, 'r') as f:
        return map(str.split, f.readlines())


if __name__ == "__main__":
    commands = read_file('day02_data.txt')
    # commands = read_file('day02_test01.txt')
    p, d = exec_commands(commands)
    print(p*d)

