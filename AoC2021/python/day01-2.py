#!/bin/env python
# Advent of Code 2021 Day 1 second
from python.utils import read_file_int as read_file


def count_inc(measures:list) -> int:
    count = 0
    prev_m = measures[2] + measures[1] + measures[0]
    for i in range(3, len(measures)):
        this_m = measures[i] + measures[i-1] + measures[i-2]
        if this_m > prev_m:
            count += 1
        print(f"{measures[i]} + {measures[i-1]} + {measures[i-2]} = {this_m} --> {prev_m}") 
        prev_m = this_m
    return count


if __name__ == "__main__":
    measures_list = read_file('day01_data01.txt')
    # measures_list = read_file('day01_test01.txt')
    print(count_inc(measures_list))
