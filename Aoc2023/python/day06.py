#
import utils


def simulate_race(race_time: int, holding_time: int) -> int:
    rest_time = race_time - holding_time
    speed = holding_time
    return speed * rest_time


def simulate_possible(race_time: int) -> [(int, int)]:
    return [simulate_race(race_time, holding_time) for holding_time in range(1, race_time)]


def winning(race_time: int, distance: int) -> [int]:
    """
    >>> list(winning(7, 9))
    [10, 12, 12, 10]
    >>> len(list(winning(71530, 940200)))
    71503
    """
    return filter(lambda d: d > distance, simulate_possible(race_time))


def part1(datas):
    """
    >>> part1(utils.read_file('../datas/06.test'))
    288
    """
    time = utils.parse_int(datas[0], start=1)
    dist = utils.parse_int(datas[1], start=1)
    mul = 1
    for i in range(len(time)):
        mul *= len(list(winning(time[i], dist[i])))
    return mul


def part2(datas):
    t = int(datas[0].replace(' ', '').split(':')[1])
    d = int(datas[1].replace(' ', '').split(':')[1])
    return len(list(winning(t, d)))


if __name__ == '__main__':
    datas = utils.read_file('../datas/06')
    print('part1', part1(datas))
    print('part2', part2(datas))
