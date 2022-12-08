def lines():
    for line in open("input.txt"):
        res = list(int(c) for c in line.strip())
        yield res


def on_colums(grid, visibles):
    nrows, ncolumns = len(grid), len(grid[0])
    for col in range(0, ncolumns):
        maxi = -1
        for row in range(0, nrows):
            if grid[row][col] > maxi:
                maxi = grid[row][col]
                if (row, col) not in visibles:
                    visibles.add((row, col))
        maxi = -1
        for row in range(nrows - 1, -1, -1):
            if grid[row][col] > maxi:
                maxi = grid[row][col]
                if (row, col) not in visibles:
                    visibles.add((row, col))


def on_rows(grid, visibles):
    nrows, ncolumns = len(grid), len(grid[0])
    for row in range(0, nrows):
        maxi = -1
        for col in range(0, ncolumns):
            if grid[row][col] > maxi:
                maxi = grid[row][col]
                if (row, col) not in visibles:
                    visibles.add((row, col))
        maxi = -1
        for col in range(ncolumns - 1, -1, -1):
            if grid[row][col] > maxi:
                maxi = grid[row][col]
                if (row, col) not in visibles:
                    visibles.add((row, col))


def solve1(grid):
    visibles = set()
    on_rows(grid, visibles)
    on_colums(grid, visibles)
    return len(visibles)


def get_view_left(grid, r, c, limit):
    if c == 0:
        return 0
    elif grid[r][c - 1] >= limit:
        return 1
    return 1 + get_view_left(grid, r, c - 1, limit)


def get_view_right(grid, r, c, limit):
    if c == len(grid[0]) - 1:
        return 0
    elif grid[r][c + 1] >= limit:
        return 1
    return 1 + get_view_right(grid, r, c + 1, limit)


def get_view_top(grid, r, c, limit):
    if r == 0:
        return 0
    elif grid[r - 1][c] >= limit:
        return 1
    return 1 + get_view_top(grid, r - 1, c, limit)


def get_view_bottom(grid, r, c, limit):
    if r == len(grid) - 1:
        return 0
    elif grid[r + 1][c] >= limit:
        return 1
    return 1 + get_view_bottom(grid, r + 1, c, limit)


def solve2(grid):
    nrows, ncolumns = len(grid), len(grid[0])
    v_left = [[-1] * ncolumns for _ in range(nrows)]
    v_right = [[-1] * ncolumns for _ in range(nrows)]
    v_top = [[-1] * ncolumns for _ in range(nrows)]
    v_bottom = [[-1] * ncolumns for _ in range(nrows)]
    for r in range(0, nrows):
        for c in range(0, ncolumns):
            v_left[r][c] = get_view_left(grid, r, c, grid[r][c])
            v_right[r][c] = get_view_right(grid, r, c, grid[r][c])
            v_top[r][c] = get_view_top(grid, r, c, grid[r][c])
            v_bottom[r][c] = get_view_bottom(grid, r, c, grid[r][c])

    score = 0
    for r in range(0, nrows):
        for c in range(0, ncolumns):
            score = max(score, v_left[r][c] * v_right[r][c] * v_top[r][c] * v_bottom[r][c])
    return score


if __name__ == "__main__":
    grid = [line for line in lines()]
    print(solve1(grid))
    print(solve2(grid))
