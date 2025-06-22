# --- Day 4: Ceres Search ---
from pprint import pprint
import re
import utils

test1 = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]


def reverse(line: str):
    return line[::-1]


def transpose(mx: list[str]) -> list[str]:
    return list(map("".join, zip(*mx)))


def diagonalize_right(mx):
    dim = len(mx)
    return ["." * i + mx[i] + "." * (dim - i) for i in range(dim)]


def diagonalize_left(mx):
    dim = len(mx)
    return ["." * (dim - i - 1) + mx[i] + "." * i for i in range(dim)]


def find_line(line: str, pattern: str) -> int:
    # print(line, line.count(pattern))
    return line.count(pattern)


def part1(data: list[str], pattern: str) -> int:
    rev_ptrn = reverse(pattern)
    s = []
    s.append(sum(map(lambda x: find_line(x, pattern), data)))
    s.append(sum(map(lambda x: find_line(x, rev_ptrn), data)))
    t_data = transpose(data)
    s.append(sum(map(lambda x: find_line(x, pattern), t_data)))
    s.append(sum(map(lambda x: find_line(x, rev_ptrn), t_data)))
    s.append(
        sum(map(lambda x: find_line(x, pattern), transpose(diagonalize_right(data))))
    )
    s.append(
        sum(map(lambda x: find_line(x, rev_ptrn), transpose(diagonalize_right(data))))
    )
    s.append(
        sum(map(lambda x: find_line(x, pattern), transpose(diagonalize_left(data))))
    )
    s.append(
        sum(map(lambda x: find_line(x, rev_ptrn), transpose(diagonalize_left(data))))
    )
    return sum(s)


def _match(a: list[str], b: list[str]) -> bool:
    r1 = re.match(a[0], b[0])
    r2 = re.match(a[1], b[1])
    r3 = re.match(a[2], b[2])
    return all([r1, r2, r3])


def part2(data: list[str], patterns: list[str]) -> int:
    s = 0
    for r in range(len(data) - 2):
        for c in range(len(data[0]) - 2):
            x = [data[r + i][c : c + 3] for i in range(3)]
            pprint(x)
            if (
                _match(patterns, x)
                or _match(transpose(patterns), x)
                or _match(list(map(reverse, transpose(patterns))), x)
                or _match(transpose(list(map(reverse, transpose(patterns)))), x)
            ):
                s += 1
    return s


if __name__ == "__main__":
    print("--- Day 4 ---")
    print("Part 1 test:", part1(test1, "XMAS"), 18)
    print("Part 2 test:", part2(test1, ["M.M", ".A.", "S.S"]), 9)
    input = utils.read_file("../datas/day04.txt")
    print("Part 1:", part1(input, "XMAS"))
    print("Part 2:", part2(input, ["M.M", ".A.", "S.S"]))
