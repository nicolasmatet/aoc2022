from collections import namedtuple

import numpy as np

Cube = namedtuple('Cube', ['pos', 'faces'])


def lines():
    for line in open("input.txt"):
        res = line.strip()
        yield np.array([[int(v)] for v in res.split(',')])


FACES = [
    np.array([[1], [0], [0]]),
    np.array([[0], [1], [0]]),
    np.array([[0], [0], [1]]),
    np.array([[-1], [0], [0]]),
    np.array([[0], [-1], [0]]),
    np.array([[0], [0], [-1]]),
]


def solve1():
    all_cubes = [Cube(pos=pos, faces=[1] * 6) for pos in lines()]
    dict_cube = {cube.pos.tobytes(): cube for cube in all_cubes}
    for cube in all_cubes:
        for idx, face in enumerate(FACES):
            if cube.faces[idx] and (neighbor := (cube.pos + face).tobytes()) in dict_cube:
                cube.faces[idx] = 0
                dict_cube[neighbor].faces[(idx + 3) % 6] = 0
    return sum(sum(cube.faces) for cube in all_cubes)


def propagate(space, start, value):
    positions = [start]
    size = len(space)
    while positions:
        current = positions.pop()
        space[tuple(current)] = value
        for face in FACES:
            neighbor = tuple((current + face) % size)
            if space[neighbor] == 0:
                positions.append((current + face) % size)

def pprint(array):
    for idx in range(len(array)):
        print(''.join(str(c) if c else '.' for c in array[idx, :]))
    print('------------------------------')
def solve2():
    all_cubes = list(lines())
    space = np.zeros(shape=(23, 23, 23), dtype=int)
    for cube in all_cubes:
        cube += np.array([[1], [1], [1]])
        space[tuple(cube)] = 2
    propagate(space, (np.array([0]), np.array([0]), np.array([0])), 1)
    surface_area = 0
    for cube in all_cubes:
        for idx, face in enumerate(FACES):
            neighbor = tuple(cube + face)
            if space[neighbor] == 1:
                surface_area += 1
    return surface_area


if __name__ == "__main__":
    # print(solve1())
    print(solve2())
