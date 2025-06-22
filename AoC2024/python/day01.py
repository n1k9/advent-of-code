import utils

def part1(list1: [int], list2: [int]) -> int:
    list1.sort()
    list2.sort()
    return sum(map(lambda e: abs(e[0]-e[1]),
        zip(list1, list2)))

def part2(list1: [int], list2: [int]) -> int:
    return sum([i * len(list(filter(lambda e: e == i, list2))) for i in list1])



assert(part1([3,4,2,1,3,3], [4,3,5,3,9,3]) == 11)
assert(part2([3,4,2,1,3,3], [4,3,5,3,9,3]) == 31)
print('OK')

if __name__ == '__main__':
    datas = utils.read_file('./datas/data-01-1.txt')
    int_datas = [utils.split_int(e) for e in datas]
    list1 = [e[0] for e in int_datas]
    list2 = [e[1] for e in int_datas]
    
    print('Part 1:', part1(list1, list2))
    print('Part 2:', part2(list1, list2))