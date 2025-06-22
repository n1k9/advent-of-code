# --- Day 10: Pipe Maze ---
import utils
Point = (int, int)
Map = [list]


# def neighbor(pos: Point,  pipe_map: Map) -> Map:
#     b = []
#     for r in range(utils.higher(pos[1] - 1), utils.lower(pos[1] + 1, len(pipe_map))):
#         b = pipe_map[r][utils.higher(pos[0] - 1):utils.lower(pos[0] + 1, len(pipe_map[r]))]
#     return b


def neighbors(pos: Point, pipe_map) -> [tuple]:
    r = min(len(pipe_map[0])-1, pos[0]) 
    c = min(len(pipe_map)-1, pos[1])
    n = (utils.higher(r - 1, 0), c)
    s = (utils.lower(r + 1, len(pipe_map)), c)
    e = (r, utils.higher(c - 1, 0))
    w = (r, utils.lower(c + 1, len(pipe_map[c])))
    match pipe_map[r][c]:
        case "|":
            return [n, s]
        case "-":
            return [e, w]
        case "L":
            return [n, w]
        case "J":
            return [n, e]
        case "7":
            return [e, s]
        case "F":
            return [s, w]
        case "S":
            dirs = []
            if pipe_map[n[0]][n[1]] in ("|", "7", "F"):
                dirs.append(n)
            if pipe_map[s[0]][s[1]] in ("|", "L", "J"):
                dirs.append(s)
            if pipe_map[w[0]][w[1]] in ("-", "L", "F"):
                dirs.append(w)
            if pipe_map[e[0]][e[1]] in ("-", "J", "7"):
                dirs.append(e)
            return dirs
        case ".":
            return []


def start_pos(datas):
    pos = None
    for r in range(len(datas)):
        for c in range(len(datas[r])):
            if datas[r][c] == 'S':
                pos = (r, c)
                break
        if pos:
            break
    return pos


def area(points: list[Point]) -> float:
    pp = [*points, points[0]]
    s = sum(r1 * c2 - r2 * c1 for (r1, c1), (r2, c2) in zip(pp, pp[1:]))
    # t = sum((pp[i][0] * pp[i+1][1] - pp[i+1][0] * pp[i][1] for i in range(len(pp)-1)))
    # print(s, t)
    return abs(s)/2


def innerpoints(datas, loop) -> int:
    count = 0
    for r in range(len(datas)):
        crosspipe = 0
        for c in range(len(datas[r])):
            if (r,c) in loop and datas[r][c] != '-':
                crosspipe += 1
            else:
                if crosspipe % 2 == 1:
                    count += 1
    return count


def solve(datas):
    """
    >>> solve(utils.read_file2('../datas/10.test'))
    (?, 10)
    """
    start_point = start_pos(datas)
    q = [start_point]
    count = 0
    visited = {}
    while q:
        node = q.pop(0)
        visited[node] = count
        for n in neighbors(node, datas):
            if n not in visited:
                q.append(n)
        count += 1
    int_point = area(list(visited.keys())) - 0.5 * count + 1
    innerpoints_count = innerpoints(datas, list(visited.keys()))
    print(innerpoints_count, int_point, count)
    return count // 2 - 1, innerpoints_count


if __name__ == '__main__':
    datas = utils.read_file2('../datas/10.test')
    p1, p2 = solve(datas)
    print('part1', p1)
    print('part2', p2)
