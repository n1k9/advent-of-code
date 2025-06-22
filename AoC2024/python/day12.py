import json
# --- Day 12: Garden Groups --
from xml.etree.ElementPath import find
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

if __name__ == "__main__":
    print("Part 1 test1:", part1(t1), 140)
    print("Part 1 test2:", part1(t2), 772)
    print("Part 1 test3:", part1(t3), 1930)

    input = utils.read_file("../datas/day12.txt")
    print("Part 1:", part1(input))
    # print("Part 2 test:", part2(t1), 2)
    # print("Part 2:", part2(input))
