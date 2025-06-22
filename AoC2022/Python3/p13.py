# --- Day 13: Distress Signal ---

from utils import read_file, to_grid


def pairs(lines: list) -> list:
    p = []
    a = b = None
    for r in lines:
        if a is None:
            a = r
        elif b is None:
            b = r
        else:
            p.append((eval(a), eval(b)))
            a = b = None
    return p


def compare(l1: list, l2: list) -> bool:
    z = zip(l1, l2)
    for a, b in z:
        # print(a, b)
        if isinstance(a, int) and isinstance(b, list):
            return compare([a], b)
        elif isinstance(a, list) and isinstance(b, int):
            return compare(a, [b])
        elif isinstance(a, list) and isinstance(b, list):
            return compare(a, b)
        elif a < b:
            return True
        elif a > b:
            return False
    if len(l1) < len(l2):
        return True
    return False


def part_1(pairs: list) -> int:
    index = 0
    in_right_order = []
    for p in pairs:
        index += 1
        if compare(p[0], p[1]):
            in_right_order.append(index)
    return sum(in_right_order)


def sort(l):
    """ Bubble Sort """
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if compare(l[i], l[j]):
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp


def part_2(l: list) -> int:
    l.append('[[2]]')
    l.append('[[6]]')
    le = list(map(eval, filter(lambda x: x != '', l)))
    sort(le)
    le.reverse()
    return (le.index([[2]])+1) * (le.index([[6]])+1)


if __name__ == "__main__":
    test_lines = read_file("../datas/d13-test.txt").split('\n')
    # print(f'Test 1: {part_1(pairs(test_lines))}')
    lines = read_file("../datas/d13.txt").split('\n')
    print(f'Part 1: {part_1(pairs(lines))}')

    # print(f'Test 2: {part_2(test_lines)})')
    print(f'Part 2: {part_2(lines)})')
