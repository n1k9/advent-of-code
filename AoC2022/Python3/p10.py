# --- Day 10: Cathode-Ray Tube ---

from utils import read_file
from functools import wraps


def int_debug(inst_method):
    @wraps(inst_method)
    def int_wrapper(self, *args, **kargs):
        # print(f"c: {self.cycle_num} {inst_method.__name__}")
        if self.cycle_num in self.interrupt_debug:
            self._signal_strength.append(self.cycle_num * self.x)
        elif self.cycle_num + 1 in self.interrupt_debug and inst_method.__name__ == 'addx':
            self._signal_strength.append((self.cycle_num + 1) * self.x)
        inst_method(self, *args, **kargs)

    return int_wrapper


def int_draw(inst_method):
    @wraps(inst_method)
    def int_wrapper(self, *args, **kargs):
        pos = self.cycle_num % 40
        pos = 40 if pos == 0 else pos
        if pos in (self.x, self.x + 1, self.x + 2):
            print("#", end="")
        else:
            print(".", end="")
        if pos == 40:
            print("\n", end="")
        if self.cycle_num == 199:
            pass

        inst_method(self, *args, **kargs)

    return int_wrapper


class Cpu:
    x: int

    def __init__(self, int_debug=[]):
        self.x = 1
        self.interrupt_debug = int_debug
        self.cycle_num = 1
        self._signal_strength = []

    @int_debug
    def addx(self, v: int):
        self._addx_1(v)
        self._addx_2(v)

    @int_draw
    def _addx_1(self, v:int):
        self.cycle_num += 1

    @int_draw
    def _addx_2(self, v: int):
        self.cycle_num += 1
        self.x += v

    @int_debug
    @int_draw
    def noop(self):
        self.cycle_num += 1

    @property
    def signal_strength(self):
        return self._signal_strength


# class Crt:
#     sprite = "###"
#     length = 40
#
#     def __init__(self):
#         self.cycle_num = 1
#         self.sprite_position = 0
#         self._line = ""
#
#     def draw(self, x):
#         if x in [self.sprite_position + 1, self.sprite_position + 2, self.sprite_position + 3]:
#             self._line += "#"
#         else:
#             self._line = "."
#         self.cycle_num += 1


def part_1(lines, interrupt=[]):
    runs = Cpu(int_debug=interrupt)
    for instr in lines:
        match instr.split():
            case ['addx', value]:
                runs.addx(int(value))
            case ['noop']:
                runs.noop()
    print(runs.signal_strength)
    return sum(runs.signal_strength)


if __name__ == "__main__":
    datas = read_file('../datas/d10-test.txt').split('\n')
    print(f"Test: {part_1(datas, interrupt=[20, 60, 100, 140, 180, 220])}")

    print(), print()
    datas = read_file('../datas/d10.txt').split('\n')
    print(f"1: {part_1(datas, interrupt=[20, 60, 100, 140, 180, 220])}")
