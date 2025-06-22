# --- Day 3: Mull It Over ---
import re

test1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

mul_re = re.compile(r"mul\(\d+,\d+\)")


def mul(a: int, b: int) -> int:
    return a * b


def part1(input):
    mul_ops = mul_re.findall(input)
    sumarize = 0
    for op in mul_ops:
        a, b = op[4:-1].split(",")
        sumarize += mul(int(a), int(b))
    return sumarize


def part2(input):
    sub = input.split("do()")
    sumarize = 0
    for s in sub:
        todo = s.split("don't()")[0]
        mul_ops = mul_re.findall(todo)
        for op in mul_ops:
            a, b = op[4:-1].split(",")
            sumarize += mul(int(a), int(b))
    return sumarize


with open("../datas/day03.txt") as f:
    input = f.read()
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
