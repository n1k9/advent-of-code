# --- Day 3: Gear Ratios ---
import re
import utils

_test = ['467..114..\n',
         '...*......\n',
         '..35..633.\n',
         '......#...\n',
         '617*......\n',
         '.....+.58.\n',
         '..592.....\n',
         '......755.\n',
         '...$.*....\n',
         '.664.598..\n']

_test2 = ['3..2......4\n',
          '*...2+....*\n',
          '10..+....1+\n']


def possible_parts(row) -> [str]:
    """
    >>> possible_parts('467..114..')
    ['467', '114']
    >>> possible_parts('...*......')
    []
    """
    return re.findall(r'\d+', row)


def possible_parts_start(row) -> [int]:
    return [i for i in range(len(row.strip())) if row[i].isdigit() and not row[i - 1].isdigit()]


def search_symbol(engine_schematic, start, part_len, row_number, symbols) -> bool:
    row_len = len(engine_schematic[row_number])
    for c in range(max(0, start - 1), min(part_len + start + 1, row_len)):
        for r in range(max(0, row_number - 1), min(row_number + 2, len(engine_schematic))):
            if engine_schematic[r][c] in symbols:
                return True
    return False


def part1(engine_schematic, symbols):
    """
    >>> part1(_test, set(re.sub(r'[\d\.\\n]*', '', ''.join(_test))))
    4361
    >>> part1(_test2, '+*')
    20
    """
    parts = []
    for r in range(len(engine_schematic)):
        possibles = possible_parts(engine_schematic[r])
        pstart = possible_parts_start(engine_schematic[r])
        for i in range(len(possibles)):
            if search_symbol(engine_schematic, pstart[i], len(possibles[i]), r, symbols):
                parts.append(int(possibles[i]))
    return sum(parts)


def possible_gear_point(row: list, symbol: str) -> [int]:
    c = []
    for i in range(len(row)):
        if row[i] == symbol:
            c.append(i)
    return c


def extract_part(row, c) -> str:
    """
    >>> extract_part('1234.....23232\\n', 2)
    '1234'
    >>> extract_part('3...\\n', 0)
    '3'
    """
    if not row[c].isdigit():
        return ''
    i = c
    while row[i].isdigit():
        i -= 1
    j = c + 1
    while j < len(row) and row[j].isdigit():
        j += 1
    return row[i+1:j]


def find_parts(es, cc) -> [int]:
    """     234
            0*1
            567
    # >>> find_parts(_test2, (1, 0) )
    # [3, 10]
    # >>> find_parts(_test2, (1, 10))
    # [4, 1]
    # >>> find_parts(_test, (1, 3))
    # [467, 35]
    # >>> find_parts(['..234*567.12.\\n',], (0, 5))
    # [567, 234]
    """
    p = []
    r, c = cc
    p.append(extract_part(es[r], c - 1))
    p.append(extract_part(es[r], c + 1))
    if r > 0:
        p.append(extract_part(es[r - 1], c - 1))
        p.append(extract_part(es[r - 1], c))
        p.append(extract_part(es[r - 1], c + 1))
    if r + 1 < len(es):
        p.append(extract_part(es[r + 1], c - 1))
        p.append(extract_part(es[r + 1], c))
        p.append(extract_part(es[r + 1], c + 1))
    return [int(x) for x in set(p) if x]


def part2(engine_schematic, symbol) -> int:
    """
    >>> part2(_test, '*')
    467835
    """
    parts = []
    for r in range(len(engine_schematic)):
        possible_gears = list(map(lambda c: (r, c), possible_gear_point(engine_schematic[r], symbol)))
        for cc in possible_gears:
            parts.append(find_parts(engine_schematic, cc))
    return sum([p[0]*p[1] for p in parts if len(p) == 2])


if __name__ == '__main__':
    datas = utils.read_file2('../datas/03')
    symbols = set(re.sub(r'[\d\.]*', '', ''.join(datas)))
    print('part1', part1(datas, symbols))
    print('part2', part2(datas, '*'))
