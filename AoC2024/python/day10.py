# --- Day 10: Hoof It ---
import utils

DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_trailhead(map: list[str]) -> list[tuple[int, int]]:
    trailhead = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "0":
                trailhead += [(i, j)]
    return trailhead


def find_path(map: list[str], start: tuple[int, int]) -> set[tuple[int, int]]:
    pos = start
    if map[pos[0]][pos[1]] == "9":
        return {pos}
    ends = set()
    for d in DIR:
        next_pos = (pos[0] + d[0], pos[1] + d[1])
        if (
            not (0 <= next_pos[0] < len(map) and 0 <= next_pos[1] < len(map[0]))
            or map[next_pos[0]][next_pos[1]] == "."
        ):
            continue
        if int(map[pos[0]][pos[1]]) + 1 == int(map[next_pos[0]][next_pos[1]]):
            ends |= find_path(map, next_pos)
    print(" >>>", start, ends)
    return ends


def find_path2(map: list[str], start: tuple[int, int]) -> int:
    pos = start
    if map[pos[0]][pos[1]] == "9":
        return 1
    count = 0
    for d in DIR:
        next_pos = (pos[0] + d[0], pos[1] + d[1])
        if (
            not (0 <= next_pos[0] < len(map) and 0 <= next_pos[1] < len(map[0]))
            or map[next_pos[0]][next_pos[1]] == "."
        ):
            continue
        if int(map[pos[0]][pos[1]]) + 1 == int(map[next_pos[0]][next_pos[1]]):
            count += find_path2(map, next_pos)
    print(" >>>", start, count)
    return count


def part1(map: list[str]) -> int:
    thead = find_trailhead(map)
    count = 0
    for start in thead:
        count += len(find_path(map, start))
    return count


def part2(map: list[str]) -> int:
    thead = find_trailhead(map)
    count = 0
    for start in thead:
        count += find_path2(map, start)
    return count


def _test1():
    t1 = [
        "...0...",
        "...1...",
        "...2...",
        "6543456",
        "7.....7",
        "8.....8",
        "9.....9",
    ]
    print("test1:", part1(t1))

    t2 = [
        "..90..9",
        "...1.98",
        "...2..7",
        "6543456",
        "765.987",
        "876....",
        "987....",
    ]
    print("P1 test2:", part1(t2))
    print("P2 test2:", part2(t2))

    t3 = [
        "10..9..",
        "2...8..",
        "3...7..",
        "4567654",
        "...8..3",
        "...9..2",
        ".....01",
    ]
    print("test3:", part1(t3))

    t4 = [
        "012345",
        "123456",
        "234567",
        "345678",
        "4.6789",
        "56789.",
    ]
    print("test4:", part2(t4))

    map = utils.read_file("../datas/day10-test.txt")
    print("Part 1 test:", part1(map))
    print("Part 2 test:", part2(map))


if __name__ == "__main__":
    # _test1()
    map = utils.read_file("../datas/day10.txt")
    print("Part 1:", part1(map))
    print("Part 2:", part2(map))
