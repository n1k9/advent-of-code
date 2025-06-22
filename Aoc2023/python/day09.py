# --- Day 9: Mirage Maintenance ---
from typing import List

import utils


def prediction(hist) -> int:
    """
    >>> prediction([0, 3, 6, 9, 12, 15])
    3
    >>> prediction([1, 3, 6, 10, 15, 21])
    7
    >>> prediction([10,  13,  16,  21,  30 , 45])
    23
    """
    h1 = []
    for i in range(len(hist)-1):
        h1.append(hist[i+1] - hist[i])
    if h1[-1] == 0:
        return 0
    return prediction(h1) + h1[-1]


def part1(datas):
    """
    >>> part1(["0 3 6 9 12 15\\n", "1 3 6 10 15 21\\n", "10 13 16 21 30 45\\n"])
    114
    """
    s = 0
    for l in datas:
        hist: list[int] = utils.parse_int(l)
        s += prediction(hist) + hist[-1]
    return s


def prediction2(hist) -> int:
    """
    >>> prediction2([10,  13,  16,  21,  30 , 45])
    5
    """
    h1 = []
    for i in range(len(hist)-1):
        h1.append(hist[i+1] - hist[i])
    if h1[-1] == 0:
        return 0
    return h1[0] - prediction2(h1)

def part2(datas):
    """
    >>> part2(["10  13  16  21  30  45\\n"])
    5
    """
    s = 0
    for l in datas:
        hist: list[int] = utils.parse_int(l)
        s += hist[0] - prediction2(hist)
    return s


if __name__ == '__main__':
    datas = utils.read_file('../datas/09')
    print('part1', part1(datas))
    print('part2', part2(datas))
