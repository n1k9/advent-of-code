#!/bin/env python
# Advent of Code 2021 Day 1 first
from python.utils import read_file_int as read_file


def count_inc(measures:list) -> int:
    count = 0
    for i in range(1, len(measures)):
        if measures[i] > measures[i-1]:
            count += 1
        # print(f"{measures[i]} > {measures[i-1]} --> {measures[i] > measures[i-1]} | {count}")
    return count


if __name__ == "__main__":
    measures_list = read_file('day01_test01.txt')
    print("TEST:", count_inc(measures_list))
    measures_list = read_file('day01_data01.txt')
    print("RESULT:", count_inc(measures_list))
