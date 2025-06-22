#!/bin/env python
# Advent of Code 2021 Day 3 first
from python.utils import read_file_str


def gamma_epsilon_rate(diagnostics):
    ones = [0]*len(diagnostics[0])
    n_recs = len(diagnostics)
    for n in diagnostics:
        signal = [int(x) for x in n.strip()]
        ones = map(sum, zip(ones, signal))
    # zeros = map(lambda a,b: a-b, [n_recs]*5, ones)
    # print (ones, zeros)
    gamma = [n > n_recs/2 for n in ones]
    epsilon = [not g for g in gamma]
    exps = [2**i for i in range(len(gamma)-1, -1, -1)]

    print(gamma, epsilon, exps, sep='\n')

    gamma_r = sum(map(lambda c, e: int(c)*e, gamma, exps))
    epsilon_r = sum(map(lambda c, e: int(c)*e, epsilon, exps))
    return gamma_r, epsilon_r


if __name__ == "__main__":
    diagnostics = read_file_str('day03_data.txt')
    # diagnostics = read_file('day03_test.txt')
    gamma, epsilon = gamma_epsilon_rate(diagnostics)

    print(gamma * epsilon)
