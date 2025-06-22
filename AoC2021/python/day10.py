#!/bin/env python
# Advent of Code 2021 Day 10
from python.utils import read_file_str as read_file

OPENER_CHARS = "([{<"
CLOSER_CHARS = ")]}>"
ERR_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
CLR_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def check_chunks(chunks, to_break=False):
    stack = []
    errors = []
    for c in chunks:
        if c in OPENER_CHARS:
            stack.append(c)
        else:
            last_opener_char = stack.pop()
            index_last_closer_char = CLOSER_CHARS.index(c)
            if last_opener_char != OPENER_CHARS[index_last_closer_char]:
                errors.append(c)
                if to_break:
                    break
    return errors


def part1(nav_cmd: list) -> int:
    error_points = 0
    for r in nav_cmd:
        errs = check_chunks(r)
        if errs:
            error_points += ERR_POINTS[errs[0]]
    return error_points


def complete_chunks(chunks):
    stack = []
    for c in chunks:
        if c in OPENER_CHARS:
            stack.append(c)
        else:
            stack.pop()
    r = ""
    while stack:
        c = stack.pop()
        r += CLOSER_CHARS[OPENER_CHARS.index(c)]
    return r


def part2(nav_cmd: list) -> int:
    points = []
    for r in nav_cmd:
        errs = check_chunks(r, to_break=True)
        if errs:
            continue
        complete = complete_chunks(r)

        point = 0
        for p in complete:
            point = point * 5 + CLR_POINTS[p]
        points.append(point)
    points.sort()
    # print(points)
    return points[len(points) // 2]


if __name__ == "__main__":
    input_test = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]"
    ]

    assert part1(input_test) == 26397
    assert part2(input_test) == 288957

    input_data = read_file('day10_data.txt')
    print(f"PART1: {part1(input_data)}")
    print(f"PART2: {part2(input_data)}")
