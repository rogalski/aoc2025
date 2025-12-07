import itertools


def max_joltage(s: list[str]) -> int:
    total_val = 0
    for bank in s:
        max_val = -1
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                value = 10 * int(bank[i]) + int(bank[j])
                if value > max_val:
                    max_val = value
        total_val += max_val
    return total_val


def max_joltage2(s: list[str]) -> int:
    """We keep two pointers, left and right. We pick leftmost available higest digit."""
    total = 0
    for bank in s:
        digits = []
        n = 12
        left = 0
        while n:
            right = len(bank) - n
            current_max_digit = -1
            current_max_idx = 0
            for k in range(right, left - 1, -1):
                if int(bank[k]) >= current_max_digit:
                    current_max_digit = int(bank[k])
                    current_max_idx = k

            digits.append(current_max_digit)
            left = current_max_idx + 1
            n -= 1

        total += sum((10**j) * digit for j, digit in enumerate(reversed(digits)))
    return total


assert max_joltage(open("day03_test.txt").read().splitlines()) == 357
print(max_joltage(open("day03_input.txt").read().splitlines()))
assert max_joltage2(open("day03_test.txt").read().splitlines()) == 3121910778619
print(max_joltage2(open("day03_input.txt").read().splitlines()))
