import math
import re

test_regex = re.compile("Test: divisible by ([0-9]+)")
if_regex = re.compile("If .+: throw to monkey ([0-9]+)")


def lines():
    for line in open("input.txt"):
        res = line.strip()
        yield res


def get_items(str_items):
    return [int(v) for v in str_items[16:].strip().split(",")]


def get_operation(str_operation):
    return eval(str_operation.strip().replace("Operation: new = ", "lambda old: "))


def get_test_clause(test):
    modulo = int(test_regex.match(test).groups()[0])
    return lambda item: item % modulo == 0


def get_then_clause(test, if_true, if_false):
    to_monkey_if_true = int(if_regex.match(if_true).groups()[0])
    to_monkey_if_false = int(if_regex.match(if_false).groups()[0])

    def then(item, monkeys):
        if test(item):
            monkeys[to_monkey_if_true].receive(item)
        else:
            monkeys[to_monkey_if_false].receive(item)

    return then


def get_monkeys():
    monkeys = []
    all_lines = lines()
    line = next(all_lines)
    idx = 0
    while True:
        if line.startswith("Monkey"):
            items = get_items(next(all_lines))
            operation = get_operation(next(all_lines))
            test = get_test_clause(next(all_lines))
            then = get_then_clause(test, next(all_lines), next(all_lines))
            monkeys.append(Monkey(idx, items, operation, then))
            idx += 1
        try:
            line = next(all_lines)
        except StopIteration:
            return monkeys


class Monkey:
    def __init__(self, idx, items, operation, then):
        self.ix = idx
        self.objects = items
        self.operation = operation
        self.then = then
        self.looked_at = 0

    def process_items(self, monkeys, manage_stress):
        for item in self.objects:
            self.looked_at += 1
            new_value = manage_stress(self.operation(item))
            self.then(new_value, monkeys)
        self.objects = []

    def receive(self, item):
        self.objects.append(item)


def monkey_business(n_round, manage_stress):
    monkeys = get_monkeys()
    for round in range(n_round):
        for monkey in monkeys:
            monkey.process_items(monkeys, manage_stress)
    most_actives = sorted(monkeys, key=lambda m: m.looked_at, reverse=True)
    return most_actives[0].looked_at * most_actives[1].looked_at


def solve1():
    manage_stress = lambda v: math.floor(v / 3)
    return monkey_business(20, manage_stress)


def solve2():
    manage_stress = lambda v: v % 9699690
    return monkey_business(10000, manage_stress)


if __name__ == "__main__":
    print(solve1())
    print(solve2())
