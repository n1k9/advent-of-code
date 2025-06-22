#!/bin/env python
from pprint import pprint
from functools import reduce


def sign_number(board, number):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                board[i][j] = str(number)
    return board


def check_win(board):
    for i in range(5):
        row_win = True
        for j in range(5):
            if not isinstance(board[i][j], str):
                row_win = False
                break
        if row_win: 
            break
    for j in range(5):
        col_win = True
        for i in range(5):
            if not isinstance(board[i][j], str):
                col_win = False
                break
        if col_win:
            break
    return row_win or col_win


def sign_boards(boards: list[list], extract_number: int):
    for i in range(len(boards)):
        boards[i] = sign_number(boards[i], extract_number)
    return boards


def sum_of_all_unmarked_numbers(board) -> int:
    s = 0
    for l in board:
        # print([x for x in l if isinstance(x, int)])
        s += sum([x for x in l if isinstance(x, int)])
    return s
    

def simulate(boards, extractions):
    for e in extractions:
        print(f"extract {e}")
        boards = sign_boards(boards, e)
        for board in boards:
            win = check_win(board)
            if win:
                s = sum_of_all_unmarked_numbers(board)
                return s * e


def read_data(filename: str):
    drawn = []
    boards = []

    with open(filename, 'r') as f:
        drawn = f.readline()
        _ = f.readline()
        board = []
        for r in f.readlines():
            if r == '\n':
                boards.append(board)
                board = []
            else:
                board.append([int(v) for v in r.strip().split()])
        else:
            if board:
                boards.append(board)
        drawn = [int(d) for d in drawn.strip().split(',')]
    return drawn, boards


if __name__ == '__main__':
    e, b = read_data('day04_data.txt')
    print('score:', simulate(b, e))
