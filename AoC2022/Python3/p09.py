# --- Day 9: Rope Bridge ---
"""
>>> part_1([('R','4'), ('U','4'), ('L','3'), ('D','1'), ('R','4'), ('D','1'), ('L','5'), ('R','2')])
13
>>> part_2([('R', '5'),('U', '8'),('L', '8'),('D', '3'),('R', '17'),('D', '10'),('L', '25'),('U', '20')])
36
>>> r = Rope(10)
>>> r.move(('R', 5))
>>> r.move(('U', 8))
>>> r.print_k()
>>> r.move(('L', 8))
>>> r.print_k()

"""

from utils import read_file, sign

R = 0
C = 1


def follow(n1: tuple, n2: tuple) -> tuple:
    """
    """
    diff_c = n1[C] - n2[C]
    diff_r = n1[R] - n2[R]
    r, c = n2
    if abs(diff_r) > 1 and abs(diff_c) > 1:
        r = n2[R] + 1 * sign(diff_r)
        c = n2[C] + 1 * sign(diff_c)
    # if diff_r == 0 and diff_c == 0:
    #     r = n2[R]
    #     c = n2[C]
    if abs(diff_r) > 1:
        r = n2[R] + 1 * sign(diff_r)
        if diff_c == 0:
            c = n2[C]
        elif abs(diff_c) == 1:
            c = n1[C]
    elif abs(diff_c) > 1:
        c = n2[C] + 1 * sign(diff_c)
        if diff_r == 0:
            r = n2[R]
        elif abs(diff_r) == 1:
            r = n1[R]


    # if n1[C] == n2[C] and n1[R] - n2[R] > 1:    # up
    #     c = n2[C]
    #     r = n2[R] + 1
    # elif n1[C] == n2[C] and n2[R] - n1[R] > 1:  # down
    #     c = n2[C]
    #     r = n2[R] - 1
    # elif n1[R] == n2[R] and n1[C] - n2[C] > 1:  # right
    #     c = n2[C] + 1
    #     r = n2[R]
    # elif n1[R] == n2[R] and n2[C] - n1[C] > 1:  # left
    #     c = n2[C] - 1
    #     r = n2[R]
    # elif abs(n1[C] - n2[C]) == 1 and n1[R] - n2[R] > 1:  # up right
    #     c = n1[C]
    #     r = n2[R] + 1
    # elif abs(n1[C] - n2[C]) == 1 and n2[R] - n1[R] > 1:  # left down
    #     c = n1[C]
    #     r = n2[R] - 1
    # elif abs(n1[R] - n2[R]) == 1 and n1[C] - n2[C] > 1:  # right up
    #     r = n1[R]
    #     c = n2[C] + 1
    # elif abs(n1[R] - n2[R]) == 1 and n2[C] - n1[C] > 1:  # left down
    #     r = n1[R]
    #     c = n2[C] - 1
    # else:
    #     print(f"{n1} {n2}")
    return r, c


class Rope:
    knots = []
    head_moves: list
    tail_moves: list

    def __init__(self, num_knots=2):
        self.num_k = num_knots
        self.knots = [(0, 0) for i in range(num_knots)]
        self.head_moves = [self.knots[0]]
        self.tail_moves = [self.knots[-1]]

    def _hold_move(self):
        self.head_moves.append(self.knots[0])
        self.tail_moves.append(self.knots[-1])

    def _tail_follow(self):
        for i in range(1, self.num_k):
            self.knots[i] = follow(self.knots[i-1], self.knots[i])

    def move(self, m):
        match m:
            case "R", i:
                [self.move_r() for _ in range(int(i))]
            case "L", i:
                [self.move_l() for _ in range(int(i))]
            case "U", i:
                [self.move_u() for _ in range(int(i))]
            case "D", i:
                [self.move_d() for _ in range(int(i))]

    def move_r(self):
        self.knots[0] = (self.knots[0][R], self.knots[0][C] + 1)
        self._tail_follow()
        self._hold_move()
        return self.knots[0]

    def move_l(self):
        self.knots[0] = (self.knots[0][R], self.knots[0][C] - 1)
        self._tail_follow()
        self._hold_move()
        return self.knots[0]

    def move_u(self):
        self.knots[0] = (self.knots[0][R] + 1, self.knots[0][C])
        self._tail_follow()
        self._hold_move()
        return self.knots[0]

    def move_d(self):
        self.knots[0] = (self.knots[0][R] - 1, self.knots[0][C])
        self._tail_follow()
        self._hold_move()
        return self.knots[0]

    def count_tail_positions(self):
        return len(set(self.tail_moves))

    def print_tail(self):
        for i in range(8, -8, -1):
            for j in range(-11, 15):
                if (i, j) == (0, 0):
                    print("s", end="")
                elif (i, j) in self.tail_moves:
                    print("#", end="")
                else:
                    print(".", end="")
            print()

    def print_k(self):
        for i in range(8, -8, -1):
            for j in range(-11, 15):
                if (i, j) in self.knots:
                    print(self.knots.index((i, j)), end="")
                else:
                    print(".", end="")
            print()


def part_1(moves: list) -> int:
    r = Rope()
    for move in moves:
        r.move(move)
    return r.count_tail_positions()


def part_2(moves: list) -> int:
    r = Rope(10)
    for move in moves:
        r.move(move)
    return r.count_tail_positions()


if __name__ == "__main__":
    datas = read_file('../datas/d09.txt').split('\n')
    moves = list(map(lambda m: m.split(), datas))

    print(f"1: {part_1(moves)}")
    print(f"2: {part_2(moves)}")
