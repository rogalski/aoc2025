def num_forkable(grid: list[list[str]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])
    forkable_count = 0
    for r in range(0, num_rows):
        for c in range(0, num_cols):
            cell = grid[r][c]
            if cell != "@":
                continue
            count_neighbors = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= num_rows or nc < 0 or nc >= num_cols:
                        continue
                    if grid[nr][nc] == "@":
                        count_neighbors += 1
            if count_neighbors < 4:
                forkable_count += 1
    return forkable_count


def num_forkable2(grid: list[str]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])
    grid = [list(row) for row in grid]
    forkable_count = 0
    while True:
        this_iter_forkable = []
        for r in range(0, num_rows):
            for c in range(0, num_cols):
                cell = grid[r][c]
                if cell != "@":
                    continue
                count_neighbors = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr = r + dr
                        nc = c + dc
                        if nr < 0 or nr >= num_rows or nc < 0 or nc >= num_cols:
                            continue
                        if grid[nr][nc] == "@":
                            count_neighbors += 1
                if count_neighbors < 4:
                    forkable_count += 1
                    this_iter_forkable.append((r, c))
        if not this_iter_forkable:
            break
        else:
            for r, c in this_iter_forkable:
                grid[r][c] = "."
    return forkable_count


assert num_forkable(open("day04_test.txt").read().splitlines()) == 13
print(num_forkable(open("day04_input.txt").read().splitlines()))
assert num_forkable2(open("day04_test.txt").read().splitlines()) == 43
print(num_forkable2(open("day04_input.txt").read().splitlines()))
