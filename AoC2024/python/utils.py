def read_file(filename: str) -> list[str]:
    lines = []
    with open(filename, "r") as h:
        lines = h.readlines()
        lines = [l.strip() for l in lines]
    return lines


def split_int(s: str) -> list[int]:
    return list(map(int, s.split()))
