from collections import defaultdict
import itertools
import os
import time


P = tuple[int, int]


def area(c: tuple[P, P]) -> int:
    (x1, y1), (x2, y2) = c
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def solve(path: str) -> tuple[tuple[P, P], int]:
    with open(path) as fh:
        points: list[P] = [tuple(map(int, line.strip().split(","))) for line in fh]

    combos = [
        (p1, p2)
        for i1, p1 in enumerate(points)
        for i2, p2 in enumerate(points)
        if i1 < i2
    ]

    max_area_combo = max(combos, key=area)
    max_area = area(max_area_combo)
    return tuple(sorted(max_area_combo)), max_area


def solve2(path: str) -> int:
    # Shapely is a cheat, I just couldn't wrap my head around it
    from shapely import Polygon

    # Due to how loop is constructed, biggest pair MUST have an index delta of two.
    with open(path) as fh:
        points: list[P] = [tuple(map(int, line.strip().split(","))) for line in fh]

    shape = Polygon(points)

    pairs = [
        (p1, p2)
        for i1, p1 in enumerate(points)
        for i2, p2 in enumerate(points)
        if i1 > i2
    ]
    area = -1
    coords = (-1, -1), (-1, -1)
    for p1, p2 in pairs:
        p3 = (p1[0], p2[1])
        p4 = (p2[0], p1[1])
        rect = Polygon([p1, p3, p2, p4])
        if shape.contains(rect):
            new_area = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)
            if new_area > area:
                area = new_area
                coords = p1, p2

    return tuple(sorted(coords)), area


assert solve("day09_test.txt") == (((2, 5), (11, 1)), 50)
print(solve("day09_input.txt"))
assert solve2("day09_test.txt") == (((2, 3), (9, 5)), 24)
print(solve2("day09_input.txt"))
# print(solve2("day09_input.txt"))
