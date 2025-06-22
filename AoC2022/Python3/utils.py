def read_file(filename: str) -> str:
    with open(filename) as f:
        s = f.read()
    return s


def to_grid(lines: list) -> list[list]:
    """
    >>> to_grid(['123', '456'])
    [['1', '2', '3'], ['4', '5', '6']]
    """
    return list(map(list, lines))


def distance(a: tuple, b: tuple) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def aggregate(s: str) -> list[list]:
    split = s.split()
    print(split)
    return split


def sign(x):
    if x >= 0:
        return 1
    else:
        return -1

if __name__ == "__main__":
    import doctest

    doctest.testmod()
