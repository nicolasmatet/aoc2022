from collections import namedtuple
from itertools import cycle
import matplotlib.pyplot as plt
import numpy as np

ROCK_SHAPE = {
    1: (np.array([0, 0, 0, 0]), np.array([0, 1, 2, 3])),
    2: (np.array([-1, 0, -1, -2, -1]), np.array([0, 1, 1, 1, 2])),
    3: (np.array([0, 0, 0, -1, -2]), np.array([0, 1, 2, 2, 2])),
    4: (np.array([0, -1, -2, -3]), np.array([0, 0, 0, 0])),
    5: (np.array([0, -1, 0, -1]), np.array([0, 0, 1, 1])),
}

Rock = namedtuple("Rock", ["type", "shape", "bounds", "contacts"])


def get_jets():
    effect = {">": +1, "<": -1}
    for line in open("input.txt"):
        res = line.strip()
        return cycle(effect[c] for c in res)


def get_rocks():
    return cycle(
        [
            Rock(1, ROCK_SHAPE[1], (1, 4), (np.array([1, 1, 1, 1]), np.array([0, 1, 2, 3]))),
            Rock(2, ROCK_SHAPE[2], (3, 3), (np.array([0, 1, 0]), np.array([0, 1, 2]))),
            Rock(3, ROCK_SHAPE[3], (3, 3), (np.array([1, 1, 1]), np.array([0, 1, 2]))),
            Rock(4, ROCK_SHAPE[4], (4, 1), (np.array([1]), np.array([0]))),
            Rock(5, ROCK_SHAPE[5], (2, 2), (np.array([1, 1]), np.array([0, 1]))),
        ]
    )


def pprint(grid, pos=None, rock=None):
    copy = np.copy(grid)
    if rock:
        copy[pos[0] + rock.shape[0], pos[1] + rock.shape[1]] = "@"
    for i in range(len(copy) - 30, len(copy)):
        print("".join(copy[i, :]))
    print("+-----------------------------------------+")


class Grid:
    def __init__(self, n):
        self.unit_of_size = 1000
        self._grid = self.empty_grid()
        self.top = len(self._grid) - 1
        self.total_top = 0

    def empty_grid(self):
        new_grid = np.ndarray(shape=(2 * self.unit_of_size, 7), dtype=object)
        new_grid[:][:] = "."
        new_grid[-1, :] = "#"
        return new_grid

    def next_step(self, pos, rock, jets):
        jet = next(jets)
        rock_blocks = pos[0] + rock.shape[0], pos[1] + rock.shape[1]
        if jet == 1 and pos[1] + rock.bounds[1] < 7 and not any(self._grid[rock_blocks[0], rock_blocks[1] + 1] == "#"):
            pos[1] += jet
        elif jet == -1 and pos[1] > 0 and not any(self._grid[rock_blocks[0], rock_blocks[1] - 1] == "#"):
            pos[1] += jet
        if any(self._grid[pos[0] + rock.contacts[0], pos[1] + rock.contacts[1]] == "#"):
            return pos, True
        pos[0] += 1
        return pos, False

    def fall(self, rock, jets):
        stop = False
        pos = np.array([self.top - 4, 2])
        while not stop:
            pos, stop = self.next_step(pos, rock, jets)
            # if not stop:
            #     pprint(self._grid, rock=rock, pos=pos)
            if stop:
                self._grid[pos[0] + rock.shape[0], pos[1] + rock.shape[1]] = "#"
                self.top = min(self.top, pos[0] - rock.bounds[0] + 1)
                # pprint(self._grid)
        if self.top < 20:
            new_grid = self.empty_grid()
            new_grid[-self.unit_of_size :, :] = self._grid[: self.unit_of_size]
            self._grid = new_grid
            self.top += len(new_grid) - self.unit_of_size
            self.total_top += len(new_grid) - self.unit_of_size


def solve_n(n):
    grid = Grid(n)
    rocks = get_rocks()
    jets = get_jets()
    start = grid.top
    for i in range(n):
        rock = next(rocks)
        grid.fall(rock, jets)
    return start - grid.top + grid.total_top


def solve2():
    pass


if __name__ == "__main__":
    # print(solve_n(2022))
    # print(solve_n(1000000000000))
    rocks = list(range(1, 100000, 10000))
    tops = [solve_n(n) - 1.57*n for n in rocks]
    plt.plot(rocks, tops)
    plt.show()