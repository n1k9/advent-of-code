# --- Day 4: Camp Cleanup ---

from utils import read_file


def split_pairs(assignment: str) -> list:
    return map(lambda p: (p[0].split('-'), p[1].split('-')), map(lambda x: x.split(","), assignment))


def in_range(a: int, low: int, high: int) -> bool:
    return low <= a <= high


def fully_contain(range_1: list, range_2: list) -> bool:
    return (in_range(int(range_1[0]), int(range_2[0]), int(range_2[1])) and
            in_range(int(range_1[1]), int(range_2[0]), int(range_2[1]))) \
           or (in_range(int(range_2[0]), int(range_1[0]), int(range_1[1])) and
               in_range(int(range_2[1]), int(range_1[0]), int(range_1[1])))


def overlaps(range_1: list, range_2: list) -> bool:
    return in_range(int(range_1[0]), int(range_2[0]), int(range_2[1])) \
            or in_range(int(range_1[1]), int(range_2[0]), int(range_2[1])) \
            or in_range(int(range_2[0]), int(range_1[0]), int(range_1[1])) \
            or in_range(int(range_2[1]), int(range_1[0]), int(range_1[1]))


if __name__ == "__main__":
    assignment = read_file('../datas/d04.txt').split('\n')
    assignment_pairs = list(split_pairs(assignment))

    # --- Part One ---
    total_full_contained = sum(map(lambda r: fully_contain(r[0], r[1]), assignment_pairs))
    print(f"1: {total_full_contained}")

    # --- Part Two ---
    total_overlap = sum(map(lambda r: overlaps(r[0], r[1]), assignment_pairs))
    print(f"2: {total_overlap}")
