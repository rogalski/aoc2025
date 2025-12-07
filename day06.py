from functools import reduce


def solve(file_path: str) -> int:
    with open(file_path) as f:
        lines = f.read().splitlines()

    split = [line.split() for line in lines]
    w = len(split[0])
    h = len(split)
    total = 0
    for i in range(w):
        nums = []
        for j in range(h - 1):
            nums.append(int(split[j][i]))
        op = split[h - 1][i]
        if op == "*":
            total += reduce(lambda x, y: x * y, nums)
        elif op == "+":
            total += sum(nums)
        else:
            raise ValueError(f"Unknown operation: {op}")
    return total


def solve2(file_path: str) -> int:
    with open(file_path) as f:
        lines = f.read().splitlines()

    w = len(lines[0].strip())
    split_indexes = [i for i in range(w) if all(line[i] == " " for line in lines)]
    split_indexes = [-1] + split_indexes + [None]
    split = [
        [line[i0 + 1 : i1] for i0, i1 in zip(split_indexes, split_indexes[1:])]
        for line in lines
    ]
    h = len(split)
    total = 0
    for i in range(len(split[0])):
        nums = []
        for j in range(h - 1):
            nums.append(split[j][i])
        op = split[h - 1][i].strip()
        # print(nums)
        max_digit_w = max(len(num) for num in nums)
        digits = [int("".join(n[ww] for n in nums)) for ww in range(max_digit_w)]
        # print(digits)
        if op == "*":
            total += reduce(lambda x, y: x * y, digits)
        elif op == "+":
            total += sum(digits)
        else:
            raise ValueError(f"Unknown operation: {op}")
    return total


assert solve("day06_test.txt") == 4277556
print(solve("day06_input.txt"))
assert solve2("day06_test.txt") == 3263827
print(solve2("day06_input.txt"))
