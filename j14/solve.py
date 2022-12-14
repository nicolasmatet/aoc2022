import numpy as np


def lines():
    for line in open("input.txt"):
        res = [tuple(map(int, n.split(","))) for n in line.strip().split(" -> ")]
        for idx, start_square in enumerate(res[:-1]):
            end_square = res[idx + 1]
            xstart, xend = start_square[1], end_square[1]
            ystart, yend = start_square[0], end_square[0]

            if xstart > xend:
                xstart, xend = xend, xstart + 1
            else:
                xend = xend + 1
            if ystart > yend:
                ystart, yend = yend, ystart + 1
            else:
                yend = yend + 1
            yield slice(xstart, xend), slice(ystart, yend)


def pprint(grid):
    for i in range(len(grid)):
        print("".join(grid[i, 450:550]))


def get_grid():
    global grid
    grid = np.ndarray(shape=(170, 700), dtype=object)
    grid[:, :] = "."
    for xslice, yslice in lines():
        grid[xslice, yslice] = "#"
    return grid


def fall(grid, x, y):
    if grid[x + 1, y] == ".":
        return x + 1, y
    if grid[x + 1, y - 1] == ".":
        return x + 1, y - 1
    if grid[x + 1, y + 1] == ".":
        return x + 1, y + 1
    grid[x, y] = "o"
    return 0, 500


def solve1(grid):
    x, y = 0, 500
    while x < len(grid) - 1:
        x, y = fall(grid, x, y)
    pprint(grid)
    return len(np.where(grid == "o")[0])


def solve2(grid):
    grid[167, :] = "#"
    x, y = 0, 500
    while grid[0, 500] != "o":
        x, y = fall(grid, x, y)
    pprint(grid)
    return len(np.where(grid == "o")[0])


if __name__ == "__main__":
    grid = get_grid()
    print(solve1(grid))
    print(solve2(grid))
