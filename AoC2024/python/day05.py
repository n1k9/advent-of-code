# --- Day 5: Print Queue ---
import utils


def _rules(a, b, rules):
    return f"{a}|{b}" in rules


def _filter_roules(p, rules):
    o = []
    for a in p:
        for b in [x for x in p if x != a]:
            if _rules(a, b, rules):
                o.append(f"{a}|{b}")
    #             pass
    return o


def _order(pages: list, rules: list):
    line_rules = _filter_roules(pages, rules)
    for i in range(len(pages) - 1):
        for j in range(i + 1, len(pages)):
            if _rules(pages[i], pages[j], line_rules):
                pages[i], pages[j] = pages[j], pages[i]
    return pages


def parts(pages, rules):
    middle = []
    ord_middle = []
    for page_list in pages:
        if all(
            [
                _rules(page_list[i], page_list[i + 1], rules)
                for i in range(len(page_list) - 1)
            ]
        ):
            middle.append(int(page_list[len(page_list) // 2]))
        else:
            ord_list = _order(page_list, rules)
            print(ord_list)
            ord_middle.append(int(ord_list[len(ord_list) // 2]))
    return sum(middle), sum(ord_middle)


if __name__ == "__main__":
    print("--- Day 5 ---")
    data = utils.read_file("../datas/day05.txt")
    i = data.index("\n")
    rules = list(map(str.strip, data[0:i]))
    pages = list(map(lambda s: s.split(","), map(str.strip, data[i + 1 :])))

    # print(rules)
    # print(pages)
    p1, p2 = parts(pages, rules)
    print("Part 1:", p1)
    print("Part 2:", p2)
