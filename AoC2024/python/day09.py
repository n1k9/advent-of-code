# --- Day 9: Disk Fragmenter ---

test0 = "12345"
test1 = "2333133121414131402"


def disposer(file) -> list:
    disk = []
    id_file = 0
    for i in range(len(file)):
        times = int(file[i])
        if i % 2 == 0:
            disk += [id_file for i in range(times)]
            id_file += 1
        else:
            disk += ["." for i in range(times)]
    return disk


def compact(line):
    disk = list(line)
    for i in range(len(disk) - 1, 0, -1):
        if disk[i] != ".":
            j = disk.index(".")
            if 0 <= j < i:
                disk[i], disk[j] = disk[j], disk[i]
            else:
                break
    return disk


def part1(line):
    disk = compact(disposer(line))
    s = 0
    for i in range(disk.index(".")):
        s += i * disk[i]
    return s


def find_free_space(disk, space_need):
    """
    >>> find_free_space(list("00...111.2....333"), 3)
    2
    >>> find_free_space(list("00...111.2....333"), 4)
    10
    """
    i = disk.index(".")
    space = ["." for _ in range(space_need)]
    while i < len(disk) - space_need:
        if disk[i : i + space_need] == space:
            return i
        i += 1
    return 0


def move_file(disk, i, j, file_size):
    if j < i:
        return
    for k in range(file_size):
        disk[i + k] = disk[j + k]
        disk[j + k] = "."


def file_size(disk, id_file):
    return disk.count(id_file)


def compact2(line) -> list:
    disk = list(line)
    id_file = disk[-1]

    while id_file > 0:
        free_space_need = file_size(disk, id_file)
        fs_index = find_free_space(disk, free_space_need)
        if fs_index > 0:
            move_file(disk, fs_index, disk.index(id_file), free_space_need)
        id_file -= 1
    return disk


def part2(line):
    disk = compact2(disposer(line))
    s = 0
    for i in range(len(disk)):
        if disk[i] != ".":
            s += i * disk[i]
    return s


print("Part 1 test 1", part1(test1))
print("Part 2 test 1", part2(test1))
line = open("../datas/day09.txt").read().strip()
print("Part 1:", part1(line))
print("part 2:", part2(line))
