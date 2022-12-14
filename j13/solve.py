from functools import cmp_to_key

from utils import stop_iteration


def lines():
    for line in open("input.txt"):
        res = line.strip()
        yield res


def get_paire():
    all_lines = lines()
    while True:
        left = eval(next(all_lines))
        right = eval(next(all_lines))
        try:
            next(all_lines)
        except StopIteration:
            yield left, right
            return
        yield left, right


def comparison(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    if isinstance(left, int):
        return comparison([left], right)
    if isinstance(right, int):
        return comparison(left, [right])
    for cleft, cright in zip(left, right):
        comparator = comparison(cleft, cright)
        if comparator:
            return comparator
    return len(left) - len(right)


def solve1():
    total = 0
    for idx, paire in enumerate(get_paire()):
        left, right = paire
        print(left, right)
        idx += 1
        if comparison(left, right) < 0:
            total += idx
    return total


def solve2():
    all_packets = [packet for paire in get_paire() for packet in paire]
    all_packets.append([[2]])
    all_packets.append([[6]])
    sorted_packets = sorted(all_packets, key=cmp_to_key(comparison))
    return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)


if __name__ == "__main__":
    print(solve1())
    print(solve2())
