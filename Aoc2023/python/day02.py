# --- Day 2: Cube Conundrum ---
from functools import reduce

import utils


def game(line: str) -> (int, [tuple]):
    """
    >>> game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
    (1, [(4, 0, 3), (1, 2, 6), (0, 2, 0)])
    """
    row = line.rsplit(":", 1)
    game_id = row[0].split()[1]
    subsets = row[1].split(";")
    game = []
    for s in subsets:
        ss = s.split(",")
        r = g = b = 0
        for c in ss:
            cc = c.strip().split()
            match cc[1]:
                case 'red':
                    r = int(cc[0])
                case 'green':
                    g = int(cc[0])
                case 'blue':
                    b = int(cc[0])
        game.append((r, g, b))
    return int(game_id), game


def is_possible(game, r, g, b) -> bool:
    """
    >>> is_possible([(4, 0, 3), (1, 2, 6), (0, 2, 0)], 4, 3, 8)
    True
    >>> is_possible([(12, 4, 0), (1, 2, 3)], 10, 10, 10)
    False
    """
    def _is_possible(t):
        return t[0] <= r and t[1] <= g and t[2] <= b
    return all(map(_is_possible, game))


def _test1():
    """
    >>> part1(["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    ...      "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    ...      "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    ...      "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    ...      "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ...      ],
    ...      12, 13, 14)
    8
    """


def part1(games, r, g, b):
    s = 0
    for gg in games:
        g_ = game(gg)
        s += g_[0] if is_possible(g_[1], r, g, b) else 0
    return s


def game_power(game_line: str) -> list:
    """
    >>> game_power("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    48
    """
    gg = game(game_line)[1]
    r = g = b = 0
    for x in gg:
        r = max(r, x[0])
        g = max(g, x[1])
        b = max(b, x[2])
    return r * g * b


def part2(games):
    powers = []
    for gg in games:
        powers.append(game_power(gg))
    return sum(powers)


if __name__ == '__main__':
    datas = utils.read_file('../datas/02')
    print('part1', part1(datas, r=12, g=13, b=14))
    print('part2', part2(datas))
