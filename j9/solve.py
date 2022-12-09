import numpy as np

DIRECTIONS = {"R": np.array([0, 1]), "L": np.array([0, -1]), "U": np.array([-1, 0]), "D": np.array([1, 0])}


def lines():
    for line in open("input.txt"):
        direction, distance = line.strip().split()
        yield direction, int(distance)


class Rope:
    def __init__(self, n_knots):
        self.knots = []
        for _ in range(n_knots):
            self.knots.append(np.array([0, 0]))

    def get_tail_delta(self, tail, head):
        delta = (head - tail) / 2
        sign = np.sign(delta)
        norm = np.floor(np.linalg.norm(delta))
        return (sign * np.ceil(sign * norm * delta)).astype(int)

    def move(self, direction):
        self.knots[0] += DIRECTIONS[direction]
        for i in range(1, len(self.knots)):
            self.knots[i] += self.get_tail_delta(self.knots[i], self.knots[i - 1])


def solve1():
    visited = set()
    rope = Rope(2)
    visited.add(tuple(rope.knots[-1]))

    for direction, distance in lines():
        for _ in range(distance):
            rope.move(direction)
            visited.add(tuple(rope.knots[-1]))
    return len(visited)


def solve2():
    visited = set()
    rope = Rope(10)
    visited.add(tuple(rope.knots[-1]))

    for direction, distance in lines():
        for _ in range(distance):
            rope.move(direction)
            visited.add(tuple(rope.knots[-1]))
    return len(visited)


if __name__ == "__main__":
    print(solve1())
    print(solve2())
