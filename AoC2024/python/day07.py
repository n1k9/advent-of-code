# --- Day 7: Bridge Repair ---
import utils
from pprint import pprint

test = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

t1 = test.splitlines()

pprint(t1)


def mul(a: int, b: int) -> int:
    return a * b


def add(a: int, b: int) -> int:
    return a + b


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def ternary(n):
    if n == 0:
        return "0"
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return "".join(reversed(nums))


def part1(lines: list) -> int:
    partials = []
    for ll in lines:
        res, terms = ll.split(": ")
        res = int(res)
        terms = list(map(int, terms.split()))
        for i in range(2 ** (len(terms) - 1)):
            _ops = bin(i)[2:].zfill(len(terms) - 1)
            ops = [mul if o == "1" else add for o in _ops]
            result = ops[0](terms[0], terms[1])
            for j in range(2, len(terms)):
                result = ops[j - 1](result, terms[j])
            if result == res:
                partials.append(result)
                break
    return sum(partials)


def part2(lines: list) -> int:
    partials = []
    for ll in lines:
        res, terms = ll.split(": ")
        res = int(res)
        terms = list(map(int, terms.split()))
        for i in range(3 ** (len(terms) - 1)):
            _ops = ternary(i).zfill(len(terms) - 1)
            ops = [mul if o == "1" else add if o == "0" else concat for o in _ops]
            result = ops[0](terms[0], terms[1])
            for j in range(2, len(terms)):
                result = ops[j - 1](result, terms[j])
            if result == res:
                partials.append(result)
                break
    return sum(partials)


print(part1(t1), 3749)
print(part2(t1), 11387)
input = utils.read_file("../datas/day07.txt")
print("Part 1:", part1(input))
print("Part 2:", part2(input))
