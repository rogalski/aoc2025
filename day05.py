def prep_input(file_path: str) -> tuple[list[tuple[int, int]], list[int]]:
    with open(file_path) as f:
        ranges, ingredients = f.read().split("\n\n")
    range_list = [tuple(map(int, line.split("-"))) for line in ranges.splitlines()]
    ingredient_list = [int(x) for x in ingredients.splitlines() if x.strip()]
    return range_list, ingredient_list


def solve(file_path: str) -> int:
    ranges, ingredients = prep_input(file_path)
    count = 0
    for ingredient in ingredients:
        counted = False
        for rmin, rmax in ranges:
            if rmin <= ingredient <= rmax:
                count += 1
                counted = True
                break
            if counted:
                break

    return count


def solve2(file_path: str) -> int:
    ranges, _ = prep_input(file_path)
    sorted_rangres = sorted(ranges, key=lambda x: x[0])
    merged_ranges = []
    for rmin, rmax in sorted_rangres:
        if not merged_ranges:
            merged_ranges.append((rmin, rmax))
        else:
            last_rmin, last_rmax = merged_ranges[-1]
            if rmin <= last_rmax + 1:
                new_rmax = max(last_rmax, rmax)
                new_range = (last_rmin, new_rmax)
                print(merged_ranges[-1], "=>", new_range, "due to", (rmin, rmax))
                merged_ranges[-1] = (last_rmin, max(last_rmax, rmax))
            else:
                merged_ranges.append((rmin, rmax))

    return sum(rmax - rmin + 1 for rmin, rmax in merged_ranges)


assert solve("day05_test.txt") == 3
print(solve("day05_input.txt"))
assert solve2("day05_test.txt") == 14
print(solve2("day05_input.txt"))
