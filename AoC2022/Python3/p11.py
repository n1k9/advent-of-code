# --- Day 11: Monkey in the Middle ---

import math
from utils import read_file

monkeys = None

def parse_op(operation):
    def prod(a, b): return a * b
    def sum2(a, b): return a + b

    op_terms = operation.split()
    t2 = op_terms[5]
    op = prod if op_terms[4] == '*' else sum2
    if t2 == 'old':
        return lambda x: op(x, x)
    else:
        return lambda x: op(x, int(t2))


def parse_test(test) -> tuple:
    test_terms = test.split()
    if test_terms[1] == 'true:':
        return True, int(test_terms[5])
    else:
        return False, int(test_terms[5])


def parse_items(str_list: list[str]) -> list[int]:
    l = []
    for i in str_list:
        l.append(int(i.replace(',', '')))
    return l


def parse_monkeys(lines):
    global monkeys
    for i in range(0, len(lines), 7):
        monkeys.append(parse_data(lines[i:i + 7]))


class Monkey:

    def __init__(self, name,
                 items=[],
                 op=None,
                 test=None,
                 if_true='',
                 if_false=''):
        self.name = name
        self.items = items
        self.op = op
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected_items = 0

    def turn(self, worry_level_divisor=3, lcm=None):
        # print(f"Monkey {self.name}:")
        while self.items:
            self.inspected_items += 1
            worry_level = self.items.pop(0)
            if lcm: worry_level %= lcm
            worry_level = self.op(worry_level)
            worry_level = worry_level // worry_level_divisor
            # print(f"  Item with worry level {worry_level} ", end='')
            if worry_level % self.test == 0:
                # print("thrown to", self.if_true)
                throw_to_monkey(worry_level, self.if_true)
            else:
                # print("thrown to", self.if_false)
                throw_to_monkey(worry_level, self.if_false)


def parse_data(monkey_lines):
    mn = monkey_lines[0].split()[1][0]
    items = parse_items(monkey_lines[1].split()[2:])
    op = parse_op(monkey_lines[2])
    test = int(monkey_lines[3].split()[3])
    if_true = parse_test(monkey_lines[4])[1]
    if_false = parse_test(monkey_lines[5])[1]
    print(mn, items, test, op, if_true, if_false)
    return Monkey(name=mn,
                  items=items,
                  op=op,
                  test=test,
                  if_true=if_true,
                  if_false=if_false)


def throw_to_monkey(item, mockey):
    global monkeys
    monkeys[mockey].items.append(item)


def print_monkey_items():
    global monkeys
    for m in monkeys:
        print(f"Monkey {m.name}: {m.items}")


def print_inspected_items():
    global monkeys
    for m in monkeys:
        print(f"Monkey {m.name} inspected items {m.inspected_items} times")


def part_1(lines):
    global monkeys
    monkeys = []
    parse_monkeys(lines)
    lcm = math.lcm(*list(map(lambda m: m.test, monkeys)))
    for t in range(20):
        for m in monkeys:
            m.turn(3, lcm)
    print_monkey_items()
    print_inspected_items()
    ii = [m.inspected_items for m in monkeys]
    ii.sort(reverse=True)
    return ii[0] * ii[1]


def part_2(lines):
    global monkeys
    monkeys = []
    parse_monkeys(lines)
    lcm = math.lcm(*list(map(lambda m: m.test, monkeys)))
    for t in range(1, 10001):
        for m in monkeys:
            m.turn(1, lcm)
        if t == 1 or t == 20 or t % 1000 == 0:
            print(f"== After round {t} ==")
            print_inspected_items()
            print()
            # print_monkey_items()
            # print()
    ii = [m.inspected_items for m in monkeys]
    ii.sort(reverse=True)
    return ii[0] * ii[1]


if __name__ == "__main__":
    lines = read_file('../datas/d11.txt').split('\n')

    print('\n Day 11')
    print(f"1: monkey business {part_1(lines)}")
    print()
    print(f"2: monkey business {part_2(lines)}")
