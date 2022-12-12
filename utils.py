from functools import reduce
from typing import Iterable, TypeVar, Callable
import numpy as np


class OrderedMaxList:
    def __init__(self, max_items):
        self.max_items = max_items
        self.values = []

    def append(self, value):
        if len(self.values) < self.max_items:
            self.values.append(value)
            return value
        if value <= self.values[0]:
            return None
        self.values[0] = value
        self.values.sort()
        return value

    def sum(self):
        return sum(self.values)


def stop_iteration(func):
    """
    :param func: function that takes an iterator and a memo value.
    Applies any operation and return new memo until iterator is empty
    :return: final memo value
    """

    def wrapper(iterator, memo):
        while True:
            try:
                memo = func(iterator, memo)
            except RuntimeError:
                return memo
            except StopIteration:
                return memo

    return wrapper


T = TypeVar("T")


def count_items(iterable: Iterable[T], where: Callable[[T], bool]):
    if not where:
        return reduce(lambda memo, _: memo + 1, iterable, 0)
    return reduce(lambda memo, _: memo + 1, filter(where, iterable), 0)


def neighbors(x, y, shape):
    nx, ny = shape
    nx -= 1
    ny -= 1
    if 0 < x < nx and 0 < y < ny:
        yield x - 1, y
        yield x, y + 1
        yield x, y - 1
        yield x + 1, y
    elif x == 0 < y < ny:
        yield x, y + 1
        yield x, y - 1
        yield x + 1, y
    elif x == nx and 0 < y < ny:
        yield x - 1, y
        yield x, y + 1
        yield x, y - 1
    elif y == 0 < x < nx:
        yield x - 1, y
        yield x, y + 1
        yield x + 1, y
    elif 0 < x < nx and y == ny:
        yield x - 1, y
        yield x, y - 1
        yield x + 1, y

    elif x == y == 0:
        yield x, y + 1
        yield x + 1, y
    elif x == 0 and y == ny:
        yield x, y - 1
        yield x + 1, y
    elif x == nx and y == ny:
        yield x - 1, y
        yield x, y - 1
    elif x == nx and y == 0:
        yield x - 1, y
        yield x, y + 1
    else:
        raise ValueError("invalid indexes")


class OrderedList:
    def __init__(self, items, key=None, reverse=False):
        self.key = key if key else lambda o: o
        self.values = items
        self.reverse = reverse

    def append(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def best(self):
        return self.values[-1]

    def sort(self):
        self.values.sort(reverse=self.reverse, key=self.key)
