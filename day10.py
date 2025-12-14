import ast
import itertools
import string
import sys


def solve(file_path: str) -> int:
    tcs = open(file_path).readlines()
    total = 0
    for tc in tcs:
        layout, *buttons, _ = tc.split()
        layout_int = sum(1 << i for i, v in enumerate(layout[1:-1]) if v == "#")
        buttons_evaled = [ast.literal_eval(b) for b in buttons]
        buttons_tuples = [(t,) if isinstance(t, int) else t for t in buttons_evaled]
        buttons_numbers = [sum(1 << i for i in t) for t in buttons_tuples]

        # shortest path from 0 to layout is the same as shortest path from layout to 0
        memory: dict[int, int] = {0: 0}
        while layout_int not in memory:
            added = 0
            for m in list(memory):
                steps = memory[m]
                for b in buttons_numbers:
                    v = m ^ b
                    if v not in memory:
                        memory[v] = steps + 1
                        added += 1
            if not added:
                raise RuntimeError("Infinite loop?", tc, memory, buttons_numbers)

        total += memory[layout_int]

    return total


def solve2(file_path: str) -> int:
    from z3 import Int, Optimize, Sum, sat

    tcs = open(file_path).readlines()
    total = 0
    for tc in tcs:
        _, *buttons, voltages = tc.split()
        target = ast.literal_eval(f"({voltages.strip('{}')})")
        buttons_evaled = [ast.literal_eval(b) for b in buttons]
        buttons_normed = [(t,) if isinstance(t, int) else t for t in buttons_evaled]
        buttons_tuples = [
            tuple(1 if i in t else 0 for i in range(len(target)))
            for t in buttons_normed
        ]

        # Still don't know if this is supposed to be linear algebra problem in integers or knapsack problem
        s = Optimize()
        ints = [Int(string.ascii_lowercase[i]) for i, _ in enumerate(buttons_tuples)]
        targets = [Int(f"t{i}") for i in range(len(target))]
        for i, t in enumerate(targets):
            s.add(t == target[i])
            s.add(
                t == Sum(*[ints[ib] for ib, b in enumerate(buttons_normed) if i in b])
            )
        for i in ints:
            s.add(i >= 0)

        s.minimize(Sum(ints))
        assert s.check() == sat
        model = s.model()
        clicks = [model[i].py_value() for i in ints]
        total += sum(clicks)

    return total


assert solve("day10_test.txt") == 7
print(solve("day10_input.txt"))
assert solve2("day10_test.txt") == 33
print(solve2("day10_input.txt"))
