# --- Day 5: If You Give A Seed A Fertilizer ---
from multiprocessing import Pool
from datetime import datetime

import utils


def build_map(rules: [list]) -> [tuple]:
    """
    >>> build_map([[50, 98, 2],
    ...            [52, 50, 3]])
    [(50, 98), (51, 99), (52, 50), (53, 51), (54, 52)]
    """
    r_ = []
    for r in rules:
        r_ += [(r[0] + i, r[1] + i) for i in range(r[2])]
    return r_


def read_seed(line) -> [int]:
    """
    >>> read_seed('seeds: 79 14 55 13\\n')
    [79, 14, 55, 13]
    """
    return utils.parse_int(line, start=1)


def parse(datas) -> dict:
    """
    >>> parse(utils.read_file('../datas/05.test')[:10])
    {'seed-to-soil': [[52, 50, 48], [50, 98, 2]], 'soil-to-fertilizer': [[39, 0, 15], [0, 15, 37], [37, 52, 2]]}
    """
    maps = {}
    actual_map = ''
    for r in datas[2:]:
        if r[0].isalpha():
            actual_map = r.strip().split()[0]
            maps[actual_map] = []
        elif r[0].isdigit():
            maps[actual_map] += [list(map(int, r.strip().split()))]
    for k in maps:
        maps[k].sort(key=lambda ru: ru[1])
    return maps


def map_to(value, map_rules) -> int:
    if value < map_rules[0][1] or value >= map_rules[-1][1] + map_rules[-1][2]:
        return value
    for i in range(0, len(map_rules)):
        mr = map_rules[i]
        if mr[1] <= value < mr[1] + mr[2]:
            return value - mr[1] + mr[0]
    return value


def process(seed, map_rules):
    step = seed
    for m in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature',
              'temperature-to-humidity', 'humidity-to-location']:
        # print(m.split('-')[0], step, end=', ')
        step = map_to(step, map_rules[m])
    return step


def part1(datas):
    """
    # seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
    # seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
    # seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
    # seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
    >>> part1(utils.read_file('../datas/05.test'))
    35
    """
    seeds = read_seed(datas[0])
    rule_maps = parse(datas)
    locations = []
    for seed in seeds:
        step = process(seed, rule_maps)
        # print("location", step, end='.\n')
        locations.append(step)
    return min(locations)


def part2(datas):
    """
    >>> part2(utils.read_file('../datas/05.test'))
    Seed: 79, range: 14
    Seed: 55, range: 13
    46
    """
    def seed_next(ranges):
        for s, n in ranges:
            print(f'Seed: {s}, range: {n}')
            for i in range(s, s+n):
                yield i

    seeds = read_seed(datas[0])
    seed_ranges = zip(seeds[::2], seeds[1::2])
    rule_maps = parse(datas)
    location = 10000000000000000
    for seed in seed_next(seed_ranges):
        step = process(seed, rule_maps)
        location = min(location, step)
    return location


if __name__ == '__main__':
    datas = utils.read_file('../datas/05')
    print('part1', part1(datas))

    start_dt = datetime.now()
    print(start_dt)
    print('part2', part2(datas))
    end_dt = datetime.now()
    print(end_dt)
    print(end_dt-start_dt)