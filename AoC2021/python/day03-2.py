#!/bin/env python
# Advent of Code 2021 Day 3 second

def counter_zeros_ones(dagnostics: list[str], position: int) -> (int, int):
    count_ones = 0
    # n_lines = len(dagnostics)
    for line in dagnostics:
        if line[position] == '1':
            count_ones += 1
    return len(dagnostics) - count_ones, count_ones

def most_common(zeros: int, ones:int) -> str:
    return '1' if ones >= zeros else '0'

def least_common(zeros: int, ones:int) -> str:
    return '1' if ones < zeros else '0'

def analize_oxygen(dagnostics: list[str], position=0) :
    zeros, ones = counter_zeros_ones(dagnostics, position)
    most_common_bit = most_common(zeros, ones)
    rest = list(filter(lambda x: x[position] == most_common_bit, dagnostics))
    if len(rest) > 1: 
        return analize_oxygen(rest, position=position+1)
    else:
        return rest[0].strip()

def CO2_scrubber_rating(dagnostics: list[str], position=0) :
    zeros, ones = counter_zeros_ones(dagnostics, position)
    least_common_bit = least_common(zeros, ones)
    rest = list(filter(lambda x: x[position] == least_common_bit, dagnostics))
    if len(rest) > 1: 
        return CO2_scrubber_rating(rest, position=position+1)
    else:
        return rest[0].strip()

def read_file(filename:str) -> list[str]:
    with open(filename, 'r') as f:
        return f.readlines()


if __name__ == "__main__":
    dagnostics = read_file('day03_data.txt')
    # dagnostics = read_file('day03_test.txt')
    oxygen_generator_rating = analize_oxygen(dagnostics)
    co2_scrubber_rating = CO2_scrubber_rating(dagnostics)
    print(f"oxygen generator rating ({oxygen_generator_rating})", int(oxygen_generator_rating, 2))
    print(f"CO2 scrubber rating     ({co2_scrubber_rating})", int(co2_scrubber_rating, 2))
    print("the life support rating of the submarine:", int(oxygen_generator_rating, 2)*int(co2_scrubber_rating, 2))
    