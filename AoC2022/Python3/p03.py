# --- Day 3: Rucksack Reorganization ---
import string

from utils import read_file

PRIORITY = string.ascii_letters + string.ascii_uppercase


def split_in_middle(s: str) -> list[str]:
    mid = len(s)//2
    return [s[:mid], s[mid:]]


def find_item(l1: str, l2: str) -> list:
    return filter(lambda x: x in l2, l1)


def intersection(a: str, b:str, c:str) -> str:
    return set(a).intersection(set(b), set(c)).pop()


if __name__ == "__main__":
    assert split_in_middle('vJrwpWtwJgWrhcsFMMfFFhFp') == ['vJrwpWtwJgWr', 'hcsFMMfFFhFp']
    assert list(find_item('vJrwpWtwJgWr', 'hcsFMMfFFhFp')).pop() == 'p'
    assert PRIORITY.index('a')+1 == 1
    assert PRIORITY.index('Z')+1 == 52
    assert intersection("vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg") == 'r'
    assert intersection("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw") == 'Z'

    rucksacks = read_file('../datas/d03.txt').split('\n')
    # --- Part One --
    rucksack_compartments = map(split_in_middle, rucksacks)
    share_items = map(lambda i: set(find_item(i[0], i[1])).pop(), rucksack_compartments)
    total_priority = sum(map(lambda c: PRIORITY.index(c)+1, share_items))
    print(f"1: {total_priority}")
    # --- Part Two ---
    badges = map(lambda group: intersection(*group), [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)])
    total_badge_priority = sum(map(lambda c: PRIORITY.index(c)+1, badges))
    print(f"2: {total_badge_priority}")
