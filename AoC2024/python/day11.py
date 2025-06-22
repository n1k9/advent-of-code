# --- day11 ---
import utils
import os


def _rule(v: int) -> list[int]:
    vs = str(v)
    if v == 0:
        return [1]
    elif len(vs) % 2 == 0:
        return [int(f"{vs[:len(vs)//2]}"), int(f"{vs[len(vs)//2:]}")]
    else:
        return [v * 2024]


def part2(line: list, blick: int) -> int:
    current = {i: 1 for i in line}
    for b in range(blick):
        new = dict()
        for n, v in current.items():
            r = _rule(n)
            for i in r:
                if i in new:
                    new[i] += 1 * v
                else:
                    new[i] = 1 * v
        current = {k: v for k, v in new.items()}
        # print("blick", b + 1, current)
    return sum(current.values())


# print(part2([125, 17], 6))
# print(part2([125, 17], 25))
with open(os.path.join("..", "datas", "day11.txt")) as f:
    line = [int(i) for i in f.read().strip().split(" ")]
print("Day 11 Part2:", part2(line, 75))
