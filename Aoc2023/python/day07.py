# --- Day 7: Camel Cards ---
from operator import itemgetter

import utils

t = {str(c): int(c) for c in range(2, 10)}
t['T'] = 10
t['J'] = 11
t['Q'] = 12
t['K'] = 13
t['A'] = 14


def hand_parse(h_string: str) -> (str, str):
    """
    >>> hand_parse("A2345 344\\n")
    ('A2345', '344')
    """
    return tuple(h_string.split())


def hand_translate(hand: str, w=t) -> tuple:
    """
    >>> hand_translate("AKQJT", t)
    (14, 13, 12, 11, 10)
    >>> hand_translate("23456", t)
    (2, 3, 4, 5, 6)
    """
    if w is None:
        w = t
    return tuple(map(lambda c: w[c], hand))


def weight(hand: str) -> tuple:
    """
    >>> weight("AAAAA")
    (5,)
    >>> weight("23332")
    (3, 2)
    """
    c = {c: 0 for c in t}
    for x in hand:
        c[x] += 1
    w = [v for v in c.values() if v > 0]
    w.sort(reverse=True)
    return tuple(w)


def part1(hands):
    """
    >>> part1(utils.read_file('../datas/07.test'))
    6440
    """
    h = []
    for hand in hands:
        p = hand_parse(hand)
        h.append([weight(p[0]), hand_translate(p[0]), int(p[1])])
    h.sort(key=itemgetter(0, 1))
    return sum([(i + 1) * h[i][2] for i in range(len(h))])


def part2(hands,):
    """
    >>> part2(utils.read_file('../datas/07.test'))
    5905
    """
    w = t.copy()
    w['J'] = 1
    h = []
    for hand in hands:
        p = hand_parse(hand)
        j_num = hand.count("J")
        w2 = list(weight(p[0]))
        if j_num and j_num != 5:
            if j_num == w2[0]:
                w2[1] += j_num
            else:
                w2[0] += j_num
            w2.remove(j_num)
        h.append([w2, hand_translate(p[0], w), int(p[1])])
    h.sort(key=itemgetter(0, 1))
    return sum([(i + 1) * h[i][2] for i in range(len(h))])


if __name__ == '__main__':
    datas = utils.read_file('../datas/07')
    print('part1', part1(datas))
    print('part2', part2(datas))
