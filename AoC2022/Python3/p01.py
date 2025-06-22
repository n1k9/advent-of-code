# --- Day 1: Calorie Counting ---

from utils import read_file


def elf_calories(lines: str) -> list:
    elf_carried = map(lambda x: x.split('\n'), lines.split('\n\n'))
    return [sum(map(int, x)) for x in elf_carried if x != ['']]


def max_carried_calories(elf_carried_list: list[int]) -> int:
    return max(elf_carried_list)


def sum_three_max_calories(elf_carried_list: list[int]) -> int:
    elf_carried_list.sort(reverse=True)
    return sum(elf_carried_list[:3])


if __name__ == '__main__':
    lines = read_file('../datas/d01.txt')
    elf_cals = elf_calories(lines)
    print(f"1: {max_carried_calories(elf_cals)}")
    print(f"2: {sum_three_max_calories(elf_cals)}")
