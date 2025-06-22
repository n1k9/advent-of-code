# --- Day 8: Resonant Collinearity ---
import utils
from functools import reduce
from pprint import pprint
import doctest

test = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def distance(a: tuple, b:tuple) -> tuple:
    """
    >>> distance((0,0), (0,0))
    (0,0)
    >>> distance((1,8), (2,5))
    (1,3)
    """
    return abs(a[0] - b[0]), abs(a[1] - b[1])

def diff(a: tuple, b:tuple) -> tuple:
    """
    >>> distance((0,0), (0,0))
    (0,0)
    >>> distance((1,8), (2,5))
    (-1,3)
    """
    return a[0] - b[0], a[1] - b[1]

def set_antinode(pos: tuple, am: list, antenna):
    if 0 <= pos[0] < len(am) and 0 <= pos[1] < len(am[0]):
        if am[pos[0]][pos[1]] == ".":
            am[pos[0]][pos[1]] = "#"
            return 1
        elif am[pos[0]][pos[1]] not in "#" + antenna:
            return 1
    return 0


def part1(antenna_map: list) -> int:
    am = [list(s.strip()) for s in antenna_map]
    antinode = set()
    for i in range(len(am)):
        for j in range(len(am[i])):
            if am[i][j] not in ".#":
                for n in range(i, len(am)):
                    for m in range(len(am[n])):
                        if am[n][m] == am[i][j]:
                            d = diff((i,j), (n,m))
                            if set_antinode((i+d[0],j+d[1]), am, am[i][j]):
                                antinode.add((i+d[0],j+d[1]))
                            if set_antinode((n-d[0],m-d[1]), am, am[n][m]):
                                antinode.add((n-d[0],m-d[1]))
    pprint([''.join(s) for s in am])
    return len(antinode)


def set_antinode2(pos: tuple, d: tuple, am: list):
    i, j = pos
    if d == (0,0):  
        return
    while 0 <= i < len(am) and 0 <= j < len(am[0]):
        if am[i][j] == ".":
            am[i][j] = "#"
        i += d[0]
        j += d[1]
    return


def part2(antenna_map: list) -> int:
    am = [list(s.strip()) for s in antenna_map]
    for i in range(len(am)):
        for j in range(len(am[i])):
            if am[i][j] not in ".#":
                for n in range(i, len(am)):
                    for m in range(len(am[n])):
                        if am[n][m] == am[i][j]:
                            d = diff((i,j), (n,m))
                            set_antinode2((i, j), d, am)
                            set_antinode2((n, m),(-d[0],-d[1]), am)
    pprint([''.join(s) for s in am])
    str_antinode = ''.join(reduce(lambda a, b: a+b, am, [])).replace(".","")
    return len(str_antinode), len(am)*len(am[0]) - reduce(lambda a, b: a+b, am, []).count(".")


test_input = test.splitlines()
print("Part 1 test:", part1(test_input), 14)
print("Part 2 test:", part2(test_input), 34)

 
input = utils.read_file("../datas/day08.txt")
print("Part 1:", part1(input))
print("Part 2:", part2(input))
