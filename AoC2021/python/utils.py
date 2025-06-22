def read_file_int(filename: str) -> list:
    with open(filename, 'r') as f:
        return list(map(int, f.readlines()))


def read_file_str(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]
