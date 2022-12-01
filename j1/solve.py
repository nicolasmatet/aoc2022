from utils import OrderedMaxList


def lines():
    for line in open("input.txt"):
        line = line.strip()
        if line:
            yield int(line)
        else:
            yield None


def get_next_sum(list_calories):
    sum_calories = 0
    try:
        while calories := next(list_calories):
            sum_calories += calories
        return sum_calories, False
    except StopIteration:
        return sum_calories, True


def get_max_n(n):
    stop = False
    max_calories = OrderedMaxList(n)
    list_calories = lines()
    while not stop:
        next_calories, stop = get_next_sum(list_calories)
        max_calories.append(next_calories)
    return max_calories.sum()


def solve1():
    print(get_max_n(1))


def solve2():
    print(get_max_n(3))


if __name__ == '__main__':
    solve1()
    solve2()
