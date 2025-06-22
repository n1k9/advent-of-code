# --- Day 2: Rock Paper Scissors ---

from Python3.utils import read_file

SCORE_1 = {
    'A': 1,     # Rock
    'B': 2,     # Paper
    'C': 3      # Scissors
}

SCORE_2 = {
    'X': 1,     # Rock
    'Y': 2,     # Paper
    'Z': 3      # Scissors
}

DEFEATS = [(1, 3), (3, 2), (2, 1)]


def round_score(a: str, b: str) -> int:
    if SCORE_1[a] == SCORE_2[b]:
        score = 3
    elif (SCORE_1[a], SCORE_2[b]) in DEFEATS:
        score = 0
    else:
        score = 6
    return SCORE_2[b] + score


def total_score(round_list: list) -> int:
    return sum(map(lambda m: round_score(m[0], m[1]) if m else 0, round_list))


def strategy(a: str, b: str) -> list:
    if b == "X":
        return [a, lose(a)]
    elif b == "Y":
        return [a, draw(a)]
    else:
        return [a, win(a)]


def lose(a: str) -> str:
    loser_score = list(filter(lambda x: SCORE_1[a] == x[0], DEFEATS)).pop()
    loser_sign = list(filter(lambda x: loser_score[1] == x[1], SCORE_2.items())).pop()
    return loser_sign[0]


def draw(a: str) -> str:
    draw_score = list(filter(lambda x: SCORE_1[a] == x[1], SCORE_2.items())).pop()
    return draw_score[0]


def win(a: str) -> str:
    win_score = list(filter(lambda x: SCORE_1[a] == x[1], DEFEATS)).pop()
    win_sign = list(filter(lambda x: win_score[0] == x[1], SCORE_2.items())).pop()
    return win_sign[0]


if __name__ == '__main__':
    lines = read_file('../datas/d02.txt')
    rounds = list(map(lambda x: x.split(), lines.split('\n')))
    print(f"1: {total_score(rounds)}")
    round_strategy = list(map(lambda m: strategy(m[0], m[1]) if m else [], rounds))
    print(f"2: {total_score(round_strategy)}")




