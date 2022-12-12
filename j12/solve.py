from collections import namedtuple

import numpy as np

from utils import neighbors, OrderedList

Path = namedtuple("Path", ["positions", "length"])


def lines():
    for line in open("input.txt"):
        res = [ord(c) for c in line.strip()]
        yield res


def is_valid_neighbor(path, neighbor, grid):
    return grid[neighbor] - grid[path.positions[-1]] < 2


def djka(paths, grid, visited):
    path = paths.pop()
    last_position = path.positions[-2] if len(path.positions) > 1 else path.positions[-1]
    current_position = path.positions[-1]
    for neighbor in neighbors(*current_position, grid.shape):
        if neighbor == last_position:
            continue
        if not is_valid_neighbor(path, neighbor, grid):
            continue
        new_path = Path(positions=[*path.positions, neighbor], length=path.length + 1)
        if visited[neighbor] > new_path.length:
            visited[neighbor] = new_path.length
            paths.append(new_path)
    paths.sort()


def solve1(grid, start, arrival):
    ended = False
    visited = np.zeros(shape=grid.shape)
    visited[:, :] = np.inf
    paths = OrderedList([Path(positions=[start], length=0)], key=lambda p: p.length, reverse=True)
    while not ended:
        djka(paths, grid, visited)
        ended = paths.best().positions[-1] == arrival
    return paths.best().length


def solve2(grid, _, arrival):
    length = np.inf
    starting_positions = zip(*np.where(grid == ord("a")))
    for start in starting_positions:
        try:
            length = min(length, solve1(grid, start, arrival))
        except IndexError:
            pass
    return length


if __name__ == "__main__":
    grid = np.array([line for line in lines()])
    start = np.where(grid == ord("S"))
    arrival = np.where(grid == ord("E"))
    grid[start] = ord("a")
    grid[arrival] = ord("z")
    start = next(zip(*start))
    arrival = next(zip(*arrival))

    print(solve1(grid, start, arrival))
    print(solve2(grid, start, arrival))
