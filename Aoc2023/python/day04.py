# --- Day 4: Scratchcards ---
import utils

_test = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n",
         "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n",
         "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n",
         "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n",
         "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n",
         "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\n"]

def extract_game(card: str) -> [[str], [str]]:
    """
    >>> extract_game("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\\n")
    [['41', '48', '83', '86', '17'], ['83', '86', '6', '31', '17', '9', '48', '53']]
    """
    c = card.rsplit(":")[1]
    winning, numbers = c.split("|")
    winning = winning.split()
    numbers = numbers.split()
    return [winning, numbers]


def winning_game(game):
    """
    >>> winning_game([['41', '48', '83', '86', '17'], ['83', '86', '6', '31', '17', '9', '48', '53']])
    ['48', '83', '86', '17']
    """
    w, g = game
    return [x for x in w if x in g]


def points(ll):
    n = len(ll)
    return 0 if n == 0 else 2**(n-1)


def part1(cards):
    """
    >>> part1(_test)
    13
    """
    pp = []
    for cg in cards:
        pp.append(points(winning_game(extract_game(cg))))
    return sum(pp)


def part2(cards):
    """
    >>> part2(_test)
    30
    """
    pp = [1 for _ in range(len(cards))]
    for i in range(len(cards)):
        wg = len(winning_game(extract_game(cards[i])))
        for j in range(i+1, i+1+wg):
            pp[j] += pp[i]
    return sum(pp)


if __name__ == '__main__':
    datas = utils.read_file('../datas/04')
    print('part1', part1(datas))
    print('part2', part2(datas))
