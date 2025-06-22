# --- Day 7: No Space Left On Device ---
from dataclasses import dataclass
from pprint import pprint

from utils import read_file


def parse_list_file(lines) -> dict:
    """

    """
    curr_path = ""
    dirs = {}
    for line in lines:
        match line.split():
            case ["$", "cd", "/"]:
                curr_path = "/"
                dirs[curr_path] = 0
            case ["$", "cd", ".."]:
                # prev_path = curr_path
                curr_path = curr_path[:curr_path.rindex('/')]
                # dirs[curr_path] += dirs[prev_path]
            case ["$", "cd", relative_path]:
                curr_path += '/' + relative_path if curr_path != '/' else relative_path
                dirs[curr_path] = 0
            case ["$", "ls"]:
                pass
            case ["dir", dir_name]:
                pass # print(f"- {dir_name}")
            case [file_size, file_name]:
                # print(f"{file_size} {file_name}")
                dirs[curr_path] += int(file_size)
    return dirs


def dirs_size(dirs: dict) -> dict:
    keys = dirs.keys()
    return {k: sum([dirs[i] for i in(filter(lambda x: k in x, keys))]) for k in keys}


def filter_less_then(dirs: dict, max_size: int) -> dict:
    return filter(lambda v: v < 100000, dirs.values())


if __name__ == "__main__":
    lines = read_file('../datas/d07.txt').split('\n')
    # lines = read_file('../datas/d07-test.txt').split('\n')

    # --- Part One ---
    d_size = dirs_size(parse_list_file(lines))
    print(f"1: {sum(filter_less_then(d_size, 100000))}")

    # --- Part Two ---
    free_space = 70000000 - d_size['/']
    space_to_free = 30000000 - free_space
    print(f"Space to free up: {space_to_free} (Free: {free_space})")
    sizes = list(d_size.values())
    sizes.sort()
    print(f"2: {list(filter(lambda x: x >= space_to_free, sizes))[0]}")
