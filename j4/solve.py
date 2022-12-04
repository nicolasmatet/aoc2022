from dataclasses import dataclass

from utils import count_items


def lines():
    for line in open("input.txt"):
        first, second = line.strip().split(",")
        start1, end1 = map(int, first.split("-"))
        start2, end2 = map(int, second.split("-"))
        yield Range(start1, end1), Range(start2, end2)


@dataclass
class Range:
    start: int
    end: int

    def __eq__(self, other):
        return self.start == other.start and other.end == self.end

    def intersection(self, other):
        min_max = min(self.end, other.end)
        max_min = max(self.start, other.start)
        if max_min > min_max:
            return None
        return Range(max_min, min_max)

    @classmethod
    def has_inclusion(cls, pair):
        range1, range2 = pair
        intersection = range1.intersection(range2)
        return intersection and (intersection == range1 or intersection == range2)

    @classmethod
    def has_intersection(cls, pair):
        range1, range2 = pair
        return range1.intersection(range2)


def solve1():
    return count_items(lines(), where=Range.has_inclusion)


def solve2():
    return count_items(lines(), where=Range.has_intersection)


if __name__ == "__main__":
    print(solve1())
    print(solve2())
