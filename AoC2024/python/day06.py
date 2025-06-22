# --- Day 6: Guard Gallivant ---
import utils
import copy
from pprint import pprint
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000000)

test1 = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]

D = "^>v<^"


def next_direction(d) -> str:
    i = D.index(d)
    return D[i + 1]


def _next(pos: tuple, dir: str) -> tuple:
    match dir:
        case "^":
            nx = pos[0] - 1, pos[1]
        case ">":
            nx = pos[0], pos[1] + 1
        case "<":
            nx = pos[0], pos[1] - 1
        case "v":
            nx = pos[0] + 1, pos[1]
        case _:
            nx = pos
    return nx


def move(pos, map: list, loop: bool = False, count: int = 0) -> bool:
    dir = map[pos[0]][pos[1]]
    nxt = _next(pos, dir)
    if pos == nxt or count > len(map) * len(map[0]):
        return False
    elif nxt[0] >= len(map) or nxt[1] >= len(map[0]) or nxt[0] < 0 or nxt[1] < 0:
        return False
    elif loop and map[nxt[0]][nxt[1]] == "O":
        return True
    elif map[nxt[0]][nxt[1]] in ("#", "O"):
        is_loop = True if loop or map[nxt[0]][nxt[1]] == "O" else False
        map[pos[0]][pos[1]] = next_direction(dir)
        return move(pos, map, is_loop, count + 1)
    else:  # map[nxt[0]][nxt[1]] not in ("#", "O"):
        map[pos[0]][pos[1]] = "X"
        map[nxt[0]][nxt[1]] = dir
        return move(nxt, map, loop, count + 1)


def find_start_position(map: list):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] in D:
                return i, j
    return None, None


def part1(guard_map: list):
    gm = guard_map
    pos = find_start_position(gm)  # noqa: F821
    print("Start:", pos)
    move(pos, gm)
    guard_str = "\n".join(map(lambda x: "".join(x), gm))
    print(guard_str)
    return guard_str.count("X") + 1  # noqa: F821


def part2(guard_map: list):
    pos = find_start_position(guard_map)
    print("Start:", pos)
    loop_count = 0
    for i in range(len(guard_map)):
        for j in range(len(guard_map[i])):
            print(i, j)
            gm = copy.deepcopy(guard_map)
            if gm[i][j] in "#" + D:
                continue
            else:
                gm[i][j] = "O"
                loop_count += 1 if move(pos, gm) else 0
            # pprint(loop_count)
            # pprint("\n".join(map(lambda x: "".join(x), gm)))
    return loop_count


if __name__ == "__main__":
    print("--- Day 6 ---")
    gm1 = [list(s.strip()) for s in test1]
    gm2 = [list(s.strip()) for s in test1]
    print("Part 1 test:", part1(gm1), 41)
    print("Part 2 test:", part2(gm2), 6)
    data = utils.read_file("../datas/day06.txt")
    input = [list(s.strip()) for s in data]
    print("Part 1:", part1(input[:]))
    # print("Part 2:", part2(input[:]))
