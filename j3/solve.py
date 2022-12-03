from functools import reduce
from itertools import islice

from utils import stop_iteration


def lines():
    for line in open("input.txt"):
        line = line.strip()
        yield Bag([c for c in line])


class Bag:
    def __init__(self, items):
        self.left = set([c for c in items[: len(items) // 2]])
        self.right = set([c for c in items[len(items) // 2 :]])
        self.items = set(items)

    def get_common(self):
        return self.left.intersection(self.right)

    @classmethod
    def get_item_value(cls, item):
        value = ord(item) - 96
        return value if value > 0 else value + 58


def solve1():
    total_values = 0
    for bag in lines():
        common_items = bag.get_common()
        total_values += sum([Bag.get_item_value(item) for item in common_items])
    return total_values


@stop_iteration
def reduce_values(all_bags, total_values_so_far):
    bag_group = islice(all_bags, 3)
    common = reduce(lambda common_items, bag: common_items.intersection(bag.items), bag_group, next(bag_group).items)
    return total_values_so_far + Bag.get_item_value(common.pop())


def solve2():
    return reduce_values(lines(), 0)


if __name__ == "__main__":
    print(solve1())
    print(solve2())
