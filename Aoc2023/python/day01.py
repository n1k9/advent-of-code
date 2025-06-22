# --- Day 1: Trebuchet?! ---
import utils


def calibration_value(s: str) -> str:
    """
    >>> calibration_value('1abc2')
    '12'
    >>> calibration_value('pqr3stu8vwx')
    '38'
    >>> calibration_value('a1b2c3d4e5f')
    '15'
    >>> calibration_value('treb7uchet')
    '77'
    """
    s1 = [c for c in s if c.isdigit()]
    return s1[0]+s1[-1]


def calibrations_sum(calibration_values: [str]) -> int:
    """
    >>> calibrations_sum(['12', '38', '15', '77'])
    142
    """
    return sum(map(int, calibration_values))


def part1(lines):
    return calibrations_sum([calibration_value(s) for s in lines])


def spell(s: str) -> str:
    """
    >>> spell('two1nine')
    '219'
    >>> spell('eightwothree')
    '823'
    >>> spell('abcone2threexyz')
    '123'
    >>> spell('xtwone3four')
    '2134'
    >>> spell('4nineeightseven2')
    '49872'
    >>> spell('zoneight234')
    '18234'
    """
    s1 = ''
    d = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
         'nine': '9'}
    for i in range(len(s)):
        if s[i].isdigit():
            s1 += s[i]
            continue
        for j in range(i+3, len(s)+1):
            if s[i:j] in d.keys():
                s1 += d[s[i:j]]
                break
    return s1


def part2(lines):
    """
    >>> part2(['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen',])
    281
    """
    return part1(list(map(spell, lines)))


if __name__ == '__main__':
    datas = utils.read_file('../datas/01')
    print('part1:', part1(datas))
    print('part2:', part2(datas))
