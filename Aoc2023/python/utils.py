def read_file(filename: str) -> [str]:
    lines = []
    with open(filename, 'r') as h:
        lines = h.readlines()
    return lines


def read_file2(filename: str) -> [str]:
    with open(filename, 'r') as h:
        lines = h.read().strip()
        return lines.split('\n')


def parse_int(line, start=0):
    return list(map(int, line.split()[start:]))


def higher(x, lower_bound=0):
    return max(x, lower_bound)


def lower(x, high_bound=0):
    return min(x, high_bound)
