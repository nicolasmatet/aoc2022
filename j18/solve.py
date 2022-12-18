import numpy as np


def lines():
    for line in open("input.txt"):
        res = line.strip()
        yield np.array([[int(v) + 1] for v in res.split(',')])


FACES = [
    np.array([[1], [0], [0]]),
    np.array([[0], [1], [0]]),
    np.array([[0], [0], [1]]),
    np.array([[-1], [0], [0]]),
    np.array([[0], [-1], [0]]),
    np.array([[0], [0], [-1]]),
]


def propagate(space, start, value):
    positions = [start]
    size = len(space)
    while positions:
        current = positions.pop()
        space[current] = value
        for face in FACES:
            neighbor = tuple((current + face) % size)
            if space[neighbor] == 0:
                positions.append(neighbor)


def solve(space, array_of_coordinates, empty_position):
    surface_area = 0
    for face in FACES:
        surface_area += sum(empty_position(space, tuple(array_of_coordinates + face)))
    return surface_area


if __name__ == "__main__":
    array_of_coordinates = np.array(list(lines())).squeeze().transpose()
    space = np.zeros(shape=(22, 22, 22), dtype=int)
    space[tuple(array_of_coordinates)] = -1
    propagate(space, (np.array([0]), np.array([0]), np.array([0])), 1)

    print(solve(space, array_of_coordinates, lambda space, pos: space[pos] >= 0))
    print(solve(space, array_of_coordinates, lambda space, pos: space[pos] == 1))
