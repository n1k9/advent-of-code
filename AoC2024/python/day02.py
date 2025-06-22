import utils

test1 = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

test2 = [6, 7, 9, 11, 13, 14, 18]

reps = list(map(utils.split_int, test1.splitlines()))


def is_safer(r: list[int]) -> tuple[bool, int]:
    asc = r[0] < r[-1]
    for i in range(1, len(r)):
        if r[i] == r[i - 1]:
            return False, i - 1
        elif asc and r[i - 1] > r[i]:
            return False, i - 1
        elif not asc and r[i - 1] < r[i]:
            return False, i - 1
        elif abs(r[i] - r[i - 1]) > 3:
            return False, i - 1
    return True, 0


def part1(reports: list[list[int]]) -> int:
    safe = 0
    for r in reports:
        if is_safer(r)[0]:
            safe += 1
    return safe


assert part1(reps) == 2


def is_safer2(r: list[int]) -> bool:
    s = is_safer(r)
    if s[0]:
        return True
    for i in range(s[1], len(r)):
        new_r = r[:i] + r[i + 1 :]
        print(r, "->", r[:i], f"<{r[i]}>", r[i + 1 :], end=" ")
        if is_safer(new_r)[0]:
            print(">> SAVE")
            return True
    print(">> UNSAFE")
    return False


def part2(reports: list[list[int]]) -> int:
    safe = 0
    for r in reports:
        if is_safer2(r):
            safe += 1
    return safe


assert part2(reps) == 4
assert part2([test2]) == 1

if __name__ == "__main__":
    reports = utils.read_file("day02.txt")
    rep_list = list(map(utils.split_int, reports))
    print(f"Part 1: {part1(rep_list)}")
    print(f"Part 2: {part2(rep_list)}")
