import functools


def count_splits(file_path: str) -> int:
    with open(file_path) as f:
        grid = [line.strip() for line in f]

    num_rows = len(grid)
    beam_cols = {i for i, c in enumerate(grid[0]) if c == "S"}
    split_count = 0
    for r in range(1, num_rows):
        beam_cols_to_add = set()
        beam_cols_to_remove = set()
        for c in beam_cols:
            if grid[r][c] == "^":
                split_count += 1
                beam_cols_to_add.add(c - 1)
                beam_cols_to_add.add(c + 1)
                beam_cols_to_remove.add(c)
        beam_cols = beam_cols - beam_cols_to_remove | beam_cols_to_add
    return split_count


def count_timelines(file_path: str) -> int:
    with open(file_path) as f:
        grid = tuple(tuple(line.strip()) for line in f)

    r = 0
    c = next(i for i, cell in enumerate(grid[0]) if cell == "S")
    return count_timelines_helper(grid, (r, c))


@functools.cache
def count_timelines_helper(
    grid: tuple[tuple[str]],
    pos: tuple[int, int],
) -> int:
    r, c = pos
    if r >= len(grid):
        return 1  # reached end, should call as valid timeline
    elif grid[r][c] == "." or grid[r][c] == "S":
        return count_timelines_helper(grid, (r + 1, c))
    elif grid[r][c] == "^":
        left = count_timelines_helper(grid, (r + 1, c - 1))
        right = count_timelines_helper(grid, (r + 1, c + 1))
        return left + right


assert count_splits("day07_test.txt") == 21
print(count_splits("day07_input.txt"))
assert count_timelines("day07_test.txt") == 40
print(count_timelines("day07_input.txt"))
