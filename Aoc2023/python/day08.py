# --- Day 8: Haunted Wasteland ---
import math

import utils
import re


def next_instruction(ins):
    i = 0
    while True:
        yield 0 if ins[i] == 'L' else 1
        i = i + 1 if i < len(ins)-1 else 0


def part1(instructions, net_map) -> int:
    """
    >>> part1('LLR', {'AAA': ('BBB', 'BBB'), 'BBB': ('AAA', 'ZZZ'), 'ZZZ': ('ZZZ', 'ZZZ')})
    6
    """
    count = 0
    current_position = 'AAA'
    while current_position != 'ZZZ':
        for i in instructions:
            current_position = net_map[current_position][0 if i == 'L' else 1]
        count += len(instructions)
    return count


def part2(instructions, net_map) -> int:
    """
    >>> part2("LR", {'11A': ('11B', 'XXX'), '11B': ('XXX', '11Z'), '11Z': ('11B', 'XXX'),'22A': ('22B', 'XXX'),'22B': ('22C', '22C'),'22C': ('22Z', '22Z'),'22Z': ('22B', '22B'),'XXX': ('XXX', 'XXX'),})
    6
    """
    counters = []
    start_positions = list(filter(lambda x: x[-1] == 'A', net_map.keys()))
    # while not all(map(lambda x: x[2] == 'Z', current_positions)):
    for start_position in start_positions:
        current_position = start_position
        count = 0
        while current_position[-1] != 'Z':
            for i in instructions:
                current_position = net_map[current_position][0 if i == 'L' else 1]
            count += len(instructions)
        counters.append(count)
    return math.lcm(*counters)


def parse_map(lines) -> dict:
    """
    >>> parse_map(['AAA = (BBB, CCC)\\n'])
    {'AAA': ('BBB', 'CCC')}
    """
    net_map = {}
    pattern = re.compile(r'([A-Z]{3}).+([A-Z]{3}).+([A-Z]{3})')
    for l in lines:
        g = pattern.match(l).groups()
        net_map[g[0]] = (g[1], g[2])
    return net_map


if __name__ == '__main__':
    datas = utils.read_file('../datas/08')
    instructions = datas[0].strip()
    net_map = parse_map(datas[2:])
    print('part1', part1(instructions, net_map))
    print('part2', part2(instructions, net_map))
