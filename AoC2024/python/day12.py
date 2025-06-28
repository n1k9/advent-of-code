# --- Day 12: Garden Groups --
import utils

t1 = [
    "AAAA",
    "BBCD",
    "BBCC",
    "EEEC",
]

t2 = [
    "OOOOO",
    "OXOXO",
    "OOOOO",
    "OXOXO",
    "OOOOO",
]

t3 = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE",
]

te = [
    "EEEEE",
    "EXXXX",
    "EEEEE",
    "EXXXX",
    "EEEEE",
]

t8 = [
    "AAAAAA",
    "AAABBA",
    "AAABBA",
    "ABBAAA",
    "ABBAAA",
    "AAAAAA",
]

def find_group(garden: list[str], pos: tuple[int, int], flower: str, visited=set()) -> set:
    """    """
    r , c = pos
    # print(f">>> {pos}")
    if not 0 <= r < len(garden) \
       or not 0 <= c < len(garden[r]) \
       or pos in visited:
        return visited
    if garden[r][c] == flower:
        visited.add(pos)
    else:
        return visited
    find_group(garden, (r + 1, c), flower, visited)
    find_group(garden, (r, c + 1), flower, visited)
    find_group(garden, (r - 1, c), flower, visited)
    find_group(garden, (r, c - 1), flower, visited)
    return visited

def find_areas(garden: list[str]) -> set[tuple]:
    areas = set()
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            area = find_group(garden, (i,j), garden[i][j], set())
            areas.add(tuple(sorted(area)))
    # print(sorted(areas))
    return areas

def calculate_prices(areas: set[tuple]) -> list[int]:
    def count_border(area: tuple):
        count = 0
        for pos in area:
            n = 0
            for neightbor in [(-1,0), (1,0), (0,1), (0,-1)]:
                # print(f"> {pos} + {neightbor} = {(pos[0]+neightbor[0], pos[1]+neightbor[1])}")
                if (pos[0]+neightbor[0], pos[1]+neightbor[1]) in area:
                    n += 1
            count += 4 - n
        return count
    area_cost = []
    for area in areas:
        area_cost.append(len(area) * count_border(area))
    return area_cost

def part1(garden: list[str]) -> int:
    """
    >>> part1(t1)
    140
    >>> part1(t2)
    772
    >>> part1(t3)
    1930
    """
    areas = find_areas(garden)
    prices = calculate_prices(areas)
    return sum(prices)

def corners(pos: tuple, area) -> int:
    """
    >>> corners((1,1), {(1,1)})
    4
    >>> corners((1,1), {(1,1), (1,2)})
    2
    >>> corners((1,2), {(1,1), (1,2), (2,2)})
    2
    >>> corners((1,2), {(1,1), (1,2), (2,2), (0, 2), (1, 3)})
    4
    >>> corners((0,0), {(0,0), (0,1), (1,0), (1,1)})
    1
    """
    n_list = []
    for neightbor in [(-1,0), (1,0), (0,1), (0,-1), (-1,-1), (-1,1), (1,1), (1,-1)]:
        # print(f"> {pos} + {neightbor} = {(pos[0]+neightbor[0], pos[1]+neightbor[1])}")
        if (pos[0]+neightbor[0], pos[1]+neightbor[1]) in area:
            n_list.append(neightbor)
    c = [
        all(((-1, 0) in n_list, (0, -1) in n_list, (-1, -1) not in n_list)),
        all(((-1, 0) not in n_list, (0, -1) not in n_list)),

        all(((0, -1) in n_list, (1, 0) in n_list, (1, -1) not in n_list)),
        all(((0, -1) not in n_list, (1, 0) not in n_list)),

        all(((1, 0) in n_list, (0, 1) in n_list, (1, 1) not in n_list)),
        all(((1, 0) not in n_list, (0, 1) not in n_list)),

        all(((0, 1) in n_list, (-1, 0) in n_list, (-1, 1) not in n_list)),
        all(((0, 1) not in n_list, (-1, 0) not in n_list))
    ]
    return c.count(True)

def part2(garden: list[str]) -> int:
    """ we know that the number of corners is equal to the number of sides
    >>> part2(t1)
    80
    """
    cost = 0
    areas = find_areas(garden)
    for area in areas:
        c = []
        for pos in area:
            c.append(corners(pos, area))
        # print(garden[area[0][0]][area[0][1]], c)
        cost += len(area) * sum(c)
    return cost

if __name__ == "__main__":
    print("Part 1 test1:", part1(t1), 140)
    print("Part 1 test2:", part1(t2), 772)
    print("Part 1 test3:", part1(t3), 1930)

    input = utils.read_file("../datas/day12.txt")
    print("Part 1:", part1(input))
    print("Part 2 test1:", part2(t1), 80)
    print("Part 2 test2:", part2(t2), 436)
    print("Part 2 test3:", part2(te), 236)
    print("Part 2 test3:", part2(t8), 368)
    print("Part 2 test3:", part2(t3), 1206)
    print("Part 2:", part2(input))
