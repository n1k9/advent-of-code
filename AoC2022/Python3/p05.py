# --- Day 5: Supply Stacks ---
import string
from pprint import pprint

from utils import read_file


def get_stack(col: int, lines: list[str]) -> list:
    return [l[col] for l in lines if col < len(l)]


def stacks_list(s: list) -> list[list]:
    return [list(filter(lambda char: char != ' ', get_stack(c, s))) for c in range(1, len(s[-1]), 4)]


def get_move(s: str) -> list:
    return list(map(int, s.replace('move', '').replace('from', '').replace('to', '').split()))


def moves_list(m: list) -> list:
    return list(map(get_move, m))


def apply_move(move, ss):
    frm = move[1] - 1
    to = move[2] - 1
    for i in range(move[0]):
        crate = ss[frm].pop(0)
        ss[to].insert(0, crate)


def apply_all(moves, stacks, func):
    for move in moves:
        func(move, stacks)
    return''.join(map(lambda f: f[0], stacks))


def apply_move2(move, ss):
    frm = move[1] - 1
    to = move[2] - 1
    crates = ss[frm][0:move[0]]
    ss[to] = crates + ss[to]
    ss[frm] = ss[frm][move[0]:]


if __name__ == "__main__":
    datas = read_file('../datas/d05.txt')
    stacks, moves = datas.split('\n\n')
    stacks_to_move = stacks_list(stacks.split('\n'))
    stacks_to_move_2 = stacks_list(stacks.split('\n'))
    moves = moves_list(moves.split('\n'))

    # --- Part One ---
    print(f"1: {apply_all(moves, stacks_to_move, apply_move)}")

    # --- Part Two ---
    print(f"2: {apply_all(moves, stacks_to_move_2, apply_move2)}")
