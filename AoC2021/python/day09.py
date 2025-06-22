# Advent of Code 2021 Day 9 first
# from python.utils import read_file
def str_to_int_list(s): return [int(c) for c in s]


def read_file(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        return [str_to_int_list(line.strip()) for line in f.readlines()]


def lower_cross_neighbors(hm, r: int, c: int) -> bool:
    p = hm[r][c]
    n = hm[r-1][c] if r-1 >= 0 else 9
    s = hm[r+1][c] if r+1 < len(hm) else 9
    w = hm[r][c-1] if c-1 >= 0 else 9
    e = hm[r][c+1] if c+1 < len(hm[r]) else 9
    return p < min(n, s, w, e)


def part1(map: list[list[int]]) -> int:
    risk_level = 0
    for r in range(len(map)):
        for c in range(len(map[r])):
            risk_level += map[r][c] + 1 if lower_cross_neighbors(map, r, c) else 0
    return risk_level


def basins_extension(hm, r, c, basin) -> list:
    if 0 <= r < len(hm) and 0 <= c < len(hm[r]):
        v = hm[r][c]

        if v < 9 and (r, c) not in basin:
            basin.append((r, c))
            if (r - 1, c) not in basin:
                basins_extension(hm, r - 1, c, basin)
            if (r + 1, c) not in basin:
                basins_extension(hm, r + 1, c, basin)
            if (r, c - 1) not in basin:
                basins_extension(hm, r, c - 1, basin)
            if (r, c + 1) not in basin:
                basins_extension(hm, r, c + 1, basin)

            return basin

    return


def part2(map: list[list[int]]) -> int:
    """ multiply together the sizes of the three largest basins
    """
    basins = []
    for r in range(len(map)):
        for c in range(len(map[r])):
            if lower_cross_neighbors(map, r, c):
                basins.append(len(basins_extension(map, r, c, [])))
    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]


if __name__ == "__main__":
    test_input = [
        str_to_int_list("2199943210"),
        str_to_int_list("3987894921"),
        str_to_int_list("9856789892"),
        str_to_int_list("8767896789"),
        str_to_int_list("9899965678")
    ]
    assert part1(test_input) == 15
    assert part2(test_input) == 1134

    input_data = read_file("day09_data.txt")
    print(f"Part1: {part1(input_data)}")
    print(f"Part2: {part2(input_data)}")
