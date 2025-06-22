# --- Day 22: Monkey Market ---
import doctest
import utils


def mix(a: int, b: int) -> int:
    """
    >>> mix(42, 15)
    37
    """
    return a ^ b


def prune(a: int) -> int:
    """
    >>> prune(100000000)
    16113920
    """
    return a % 16777216


def seq_next(a: int) -> int:
    """
    >>> seq_next(123)
    15887950
    >>> seq_next(15887950)
    16495136
    """
    a = prune(mix(a, (a * 64)))
    a = prune(mix(a, (a // 32)))
    a = prune(mix(a, (a * 2048)))
    return a


def part1(data: list[int], iterations: int = 2000) -> int:
    secrets = []
    for a in data:
        sec = a
        for i in range(iterations):
            sec = seq_next(sec)
        secrets.append(sec)
        print(f"{a}: {sec}")
    return sum(secrets)


doctest.testmod()
assert part1([1, 10, 100, 2024]) == 37327623
lines = utils.read_file("../datas/day22.txt")
datas = list(map(int, lines))
print("Part1:", part1(datas))
