# --- Day 12: Hill Climbing Algorithm ---
import string
from dataclasses import dataclass
from pprint import pprint
from queue import PriorityQueue

from utils import read_file, to_grid

INFINITE = 1000
height_values = 'S' + string.ascii_lowercase + 'E'


@dataclass
class Position:
    row: int
    col: int

    def up(self):
        return Position(self.row - 1, self.col)

    def down(self):
        return Position(self.row + 1, self.col)

    def right(self):
        return Position(self.row, self.col + 1)

    def left(self):
        return Position(self.row, self.col - 1)

    def __hash__(self):
        return self.row * 1000 + self.col

    def __gt__(self, other) -> bool:
        return (self.row, self.col) > (other.row, other.col)

    def __lt__(self, other) -> bool:
        return (self.row, self.col) < (other.row, other.col)


class HeightMap:
    hmap: list[list]
    row_len: int
    col_len: int

    def __init__(self, hmap: list[list]):
        self.hmap = hmap
        self.row_len = len(self.hmap)
        self.col_len = len(self.hmap[0])

    def find_pos(self, elem: str) -> Position:
        for r in range(self.row_len):
            for c in range(self.col_len):
                if self.hmap[r][c] == elem:
                    return Position(row=r, col=c)
        return None

    def get_height(self, pos: Position) -> int:
        if 0 <= pos.row < self.row_len and 0 <= pos.col < self.col_len:
            return self._height(self.hmap[pos.row][pos.col])
        else:
            return INFINITE

    def get(self, pos: Position) -> str:
        if 0 <= pos.row < self.row_len and 0 <= pos.col < self.col_len:
            return self.hmap[pos.row][pos.col]
        else:
            return ''

    def set_path(self, pos: Position, val):
        self.hmap[pos.row][pos.col] = val
        return val

    def print_map(self, path=[]):
        for r in range(self.row_len):
            for c in range(self.col_len):
                if Position(r, c) in path:
                    print(self.hmap[r][c].upper(), end='')
                else:
                    print(self.hmap[r][c], end='')
            print()

    def neighbors(self, pos: Position) -> list[Position]:
        n = []
        h_pos = self.get_height(pos)
        if (self.get_height(pos.right()) - h_pos) <= 1:
            n.append(pos.right())
        if (self.get_height(pos.up()) - h_pos) <= 1:
            n.append(pos.up())
        if (self.get_height(pos.down()) - h_pos) <= 1:
            n.append(pos.down())
        if (self.get_height(pos.left()) - h_pos) <= 1:
            n.append(pos.left())
        return n

    @staticmethod
    def distance(p1: Position, p2: Position) -> int:
        return abs(p2.row - p1.row) + abs(p2.col - p1.col)

    @staticmethod
    def _height(s) -> int:
        match s:
            case 'S':
                h = height_values.index('a')
            case 'E':
                h = height_values.index('z')
            case other:
                h = height_values.index(s)
        return h

    def cost(self, p1: Position, p2: Position):
        return 1


def reconstruct_path(came_from, current, start):
    total_path = []
    while current != start:
        total_path.insert(0, current)
        current = came_from[current]
    return total_path


def heuristic(a: Position, b: Position) -> int:
    # Manhattan distance on a square grid
    return abs(a.row - b.row) + abs(a.col - b.col)


def a_star(graph, start, goal, h=heuristic):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = dict()
    came_from[start] = None
    cost_so_far = dict()
    cost_so_far[start] = 0
    closedset = set()

    while not frontier.empty():
        current = frontier.get()[1]
        closedset.add(current)
        if current == goal:
            return reconstruct_path(came_from, current, start)

        for next in graph.neighbors(current):
            if next in closedset:
                continue
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + h(goal, next)
                frontier.put((priority, next))
                came_from[next] = current

    return None


def part_1(height_map: HeightMap) -> int:
    start_pos = hmap.find_pos('S')
    end_pos = hmap.find_pos('E')
    path = a_star(hmap, start_pos, end_pos)
    return len(path) if path else INFINITE


def part_2(height_map: HeightMap) -> int:
    end_pos = hmap.find_pos('E')
    starts_len = []
    for r in range(height_map.row_len):
        for c in range(height_map.col_len):
            p = Position(r, c)
            if height_map.get(Position(r, c)) in ['a', 'S']:
                path = a_star(height_map, p, end_pos)
                if path:
                    starts_len.append(len(path))
    return min(starts_len)


if __name__ == "__main__":
    hmap = HeightMap(to_grid(read_file('../datas/d12.txt').split('\n')))

    pprint(a_star(hmap, Position(40, 47), Position(20,40)))

    print(f"1: {part_1(hmap)}")
    print(f"2: {part_2(hmap)}")
