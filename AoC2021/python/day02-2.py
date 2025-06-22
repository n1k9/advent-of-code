#!/bin/env python
# Advent of Code 2021 Day 2 second
# from python.utils import read_file


def exec_commands(commands):
    pos = depth = aim = 0
    for c,val in commands:
        if c == 'forward':
            pos += int(val)
            depth += int(val) * aim
        elif c == 'up':
            aim -= int(val)
        elif c == 'down':
            aim += int(val)

    return pos, depth


def read_file(filename:str) -> list:
    with open(filename, 'r') as f:
        return map(str.split, f.readlines())


if __name__ == "__main__":
    commands = read_file('day02_data.txt')
    # commands = read_file('day02_test01.txt')
    p, d = exec_commands(commands)
    print(p,d,p*d)

