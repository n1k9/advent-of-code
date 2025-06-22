# --- Day 19: Linen Layout ---
from functools import cache


def part1(lines) -> int:
    def in_patterns(design: str, patterns: list[str]) -> bool:
        """
        >>> patterns = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
        >>> in_patterns("brwrr", patterns)
        True
        >>> in_patterns("bggr", patterns)
        True
        >>> in_patterns("ubwu", patterns)
        False
        >>> in_patterns("bwurrg", patterns)
        True
        """
        if design == "":
            return True
        else:
            return any(
                design.startswith(p) and in_patterns(design[len(p) :], patterns)
                for p in patterns
            )

    patterns = list(map(str.strip, lines[0].split(",")))
    # patterns = sorted(patterns, key=len, reverse=True)
    design = list(map(str.strip, lines[2:]))
    # print(patterns)
    # print(design)
    return sum([1 for d in design if in_patterns(d, patterns)])


def part2(lines) -> int:
    patterns = list(map(str.strip, lines[0].split(",")))
    design = list(map(str.strip, lines[2:]))

    @cache
    def count_patterns(design: str) -> int:
        """
        >>> patterns = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
        >>> in_patterns("brwrr", patterns)
        2
        >>> in_patterns("bggr", patterns)
        1
        >>> in_patterns("ubwu", patterns)
        0
        >>> in_patterns("bwurrg", patterns)
        1
        >>> in_patterns("rrbgbr", patterns)
        6
        """
        if design == "":
            return 1
        else:
            return sum(
                [
                    count_patterns(design[len(p) :])
                    for p in patterns
                    if design.startswith(p)
                ]
            )

    return sum(count_patterns(d) for d in design)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    with open("../datas/day19.txt") as f:
        lines = f.readlines()
    # in_patterns("bwurrg", ["r", "wr", "b", "g", "rb", "gb", "br", "bwu"])

    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
